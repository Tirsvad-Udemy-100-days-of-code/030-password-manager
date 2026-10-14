"""@brief Capture the README and wiki screenshots of the real Tkinter window.

@file capture_screenshots.py
@details Windows only (GDI through ctypes), standard library only. Each state
runs in its own process, uses a temporary data file and never touches the
user's `data.json`. Only the windows of the program itself are rendered
(`PrintWindow`) onto a neutral canvas, so nothing from the desktop appears.
Usage, from the repository root with the venv active:

    python tools/capture_screenshots.py            # writes docs/images/*.png
    python tools/capture_screenshots.py --out DIR  # another output folder
"""

import argparse
import ctypes
import os
import struct
import subprocess
import sys
import tempfile
import tkinter as tk
import zlib
from ctypes import wintypes
from pathlib import Path

STATES = {
    "main-window": "Window after Generate Password",
    "add-confirmation": "Confirmation before an entry is saved",
    "search-found": "Search finds a saved website",
    "search-not-found": "Search for an unknown website",
}
SAMPLE_WEBSITE = "example.com"
SAMPLE_EMAIL = "jens@example.com"
SAMPLE_PASSWORD = "Sample#Pass123"
UNKNOWN_WEBSITE = "unknown.org"
PADDING = 24
CANVAS_PIXEL = bytes([0xEE, 0xEE, 0xEE, 0xFF])
CAPTURE_DELAY_MS = 900
PW_RENDERFULLCONTENT = 2
DWMWA_EXTENDED_FRAME_BOUNDS = 9


class BitmapInfoHeader(ctypes.Structure):
    """@brief Win32 BITMAPINFOHEADER."""

    _fields_ = [
        ("biSize", wintypes.DWORD),
        ("biWidth", wintypes.LONG),
        ("biHeight", wintypes.LONG),
        ("biPlanes", wintypes.WORD),
        ("biBitCount", wintypes.WORD),
        ("biCompression", wintypes.DWORD),
        ("biSizeImage", wintypes.DWORD),
        ("biXPelsPerMeter", wintypes.LONG),
        ("biYPelsPerMeter", wintypes.LONG),
        ("biClrUsed", wintypes.DWORD),
        ("biClrImportant", wintypes.DWORD),
    ]


def write_png(path: Path, width: int, height: int, bgra: bytes) -> None:
    """@brief Write a BGRA pixel buffer as an RGB PNG file.

    @param path Output file.
    @param width Image width in pixels.
    @param height Image height in pixels.
    @param bgra Raw pixels, 4 bytes each, top row first.
    """
    stride = width * 4
    raw = bytearray()
    for y in range(height):
        row = bgra[y * stride : (y + 1) * stride]
        raw.append(0)
        raw += bytes(
            channel
            for x in range(width)
            for channel in (row[x * 4 + 2], row[x * 4 + 1], row[x * 4])
        )

    def chunk(kind: bytes, data: bytes) -> bytes:
        body = kind + data
        checksum = zlib.crc32(body) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + body + struct.pack(">I", checksum)

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", header)
        + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def render_window(hwnd: int, width: int, height: int) -> bytes:
    """@brief Render one window's own pixels (never the desktop behind it).

    @param hwnd Window handle.
    @param width Window width in pixels.
    @param height Window height in pixels.
    @return Raw BGRA pixels, top row first.
    """
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32
    screen_dc = user32.GetDC(0)
    memory_dc = gdi32.CreateCompatibleDC(screen_dc)
    bitmap = gdi32.CreateCompatibleBitmap(screen_dc, width, height)
    gdi32.SelectObject(memory_dc, bitmap)
    user32.PrintWindow(hwnd, memory_dc, PW_RENDERFULLCONTENT)
    info = BitmapInfoHeader(
        ctypes.sizeof(BitmapInfoHeader), width, -height, 1, 32, 0, 0, 0, 0, 0, 0
    )
    buffer = ctypes.create_string_buffer(width * height * 4)
    gdi32.GetDIBits(memory_dc, bitmap, 0, height, buffer, ctypes.byref(info), 0)
    gdi32.DeleteObject(bitmap)
    gdi32.DeleteDC(memory_dc)
    user32.ReleaseDC(0, screen_dc)
    return buffer.raw


def own_windows() -> list[int]:
    """@brief Visible top-level windows of this process, topmost first.

    @return Window handles.
    """
    user32 = ctypes.windll.user32
    found: list[int] = []
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    def visit(hwnd: int, _lparam: int) -> bool:
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value == os.getpid() and user32.IsWindowVisible(hwnd):
            found.append(hwnd)
        return True

    user32.EnumWindows(callback_type(visit), 0)
    return found


def frame_and_window(hwnd: int) -> tuple[wintypes.RECT, wintypes.RECT]:
    """@brief Visible frame and full window rectangle of a window.

    @param hwnd Window handle.
    @return The extended frame bounds and the GetWindowRect rectangle.
    """
    frame, outer = wintypes.RECT(), wintypes.RECT()
    ctypes.windll.dwmapi.DwmGetWindowAttribute(
        hwnd, DWMWA_EXTENDED_FRAME_BOUNDS, ctypes.byref(frame), ctypes.sizeof(frame)
    )
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(outer))
    return frame, outer


def compose_windows() -> tuple[int, int, bytes]:
    """@brief Render this process's windows side by side on a neutral canvas.

    @return Canvas width, height and BGRA pixels.
    """
    pieces = []
    for hwnd in own_windows():
        frame, outer = frame_and_window(hwnd)
        width, height = outer.right - outer.left, outer.bottom - outer.top
        pixels = render_window(hwnd, width, height)
        offset_x, offset_y = frame.left - outer.left, frame.top - outer.top
        piece_width = frame.right - frame.left
        piece_height = frame.bottom - frame.top
        rows = [
            pixels[((offset_y + y) * width + offset_x) * 4 :][: piece_width * 4]
            for y in range(piece_height)
        ]
        pieces.append((frame.left, frame.top, piece_width, piece_height, rows))
    left = min(piece[0] for piece in pieces) - PADDING
    top = min(piece[1] for piece in pieces) - PADDING
    right = max(piece[0] + piece[2] for piece in pieces) + PADDING
    bottom = max(piece[1] + piece[3] for piece in pieces) + PADDING
    width, height = right - left, bottom - top
    canvas = [bytearray(CANVAS_PIXEL * width) for _ in range(height)]
    for x, y, piece_width, _piece_height, rows in reversed(pieces):
        for index, row in enumerate(rows):
            start = (x - left) * 4
            canvas[y - top + index][start : start + piece_width * 4] = row
    return width, height, b"".join(bytes(row) for row in canvas)


def run_state(state: str, out_file: Path) -> None:
    """@brief Show the window in one state, capture it and exit the process.

    @param state One of the keys of STATES.
    @param out_file PNG file to write.
    """
    ctypes.windll.user32.SetProcessDPIAware()
    from password_manager.application.use_cases import (
        FindPasswordEntry,
        GeneratePassword,
        SavePasswordEntry,
    )
    from password_manager.domain.password_entry import PasswordEntry
    from password_manager.infrastructure.persistence.json_password_repository import (
        JsonPasswordRepository,
    )
    from password_manager.presentation.features.password_manager import (
        password_manager_view as view_module,
    )
    from password_manager.presentation.features.password_manager import (
        password_manager_view_model as view_model_module,
    )

    with tempfile.TemporaryDirectory() as folder:
        repository = JsonPasswordRepository(Path(folder) / "data.json")
        repository.add(PasswordEntry(SAMPLE_WEBSITE, SAMPLE_EMAIL, SAMPLE_PASSWORD))
        view_model = view_model_module.PasswordManagerViewModel(
            SavePasswordEntry(repository),
            FindPasswordEntry(repository),
            GeneratePassword(),
        )
        root = tk.Tk()
        view = view_module.PasswordManagerView(root, view_model)
        root.geometry("+120+120")

        def capture() -> None:
            width, height, pixels = compose_windows()
            write_png(out_file, width, height, pixels)
            os._exit(0)

        def act() -> None:
            website = UNKNOWN_WEBSITE if state == "search-not-found" else SAMPLE_WEBSITE
            view.website_entry.insert(0, website)
            if state == "main-window":
                view.generate_password()
                root.after(CAPTURE_DELAY_MS, capture)
                return
            root.after(CAPTURE_DELAY_MS, capture)
            if state == "add-confirmation":
                view.password_entry.insert(0, SAMPLE_PASSWORD)
                view.save()
            else:
                view.find_password()

        root.after(400, act)
        root.mainloop()


def main() -> None:
    """@brief Capture every state, each in a child process."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("docs/images"))
    parser.add_argument("--state", choices=sorted(STATES), help="internal use")
    parser.add_argument("--file", type=Path, help="internal use")
    args = parser.parse_args()
    if args.state:
        run_state(args.state, args.file)
        return
    args.out.mkdir(parents=True, exist_ok=True)
    for state in STATES:
        target = args.out / f"{state}.png"
        subprocess.run(
            [sys.executable, __file__, "--state", state, "--file", str(target)],
            check=True,
            timeout=60,
        )
        print(f"wrote {target}")


if __name__ == "__main__":
    main()
