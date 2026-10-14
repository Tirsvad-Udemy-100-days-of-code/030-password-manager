[English](Installation) · [Dansk](Installation-da) · **Bahasa Malaysia**

# Pemasangan

## Keperluan

- Python 3.13 atau lebih baharu dengan Tkinter. Pada Debian atau Ubuntu pasang
  `python3-tk`.
- `venv` dan `pip`, kedua-duanya sebahagian daripada Python.
- Tiada kebergantungan semasa dijalankan.

## Cipta persekitaran maya tempatan

Windows (PowerShell):

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Tambahan `[dev]` memasang pytest dan ruff. Tinggalkannya
(`python -m pip install -e .`) jika anda hanya mahu menjalankan program.

## Semak pemasangan

```bash
python -m pytest
```
