import tkinter as tk
from collections.abc import Iterator
from pathlib import Path

import pytest

from password_manager import constants
from password_manager.application.use_cases import (
    FindPasswordEntry,
    GeneratePassword,
    SavePasswordEntry,
)
from password_manager.infrastructure.persistence.json_password_repository import (
    JsonPasswordRepository,
)
from password_manager.presentation.features.password_manager import (
    password_manager_view as view_module,
)
from password_manager.presentation.features.password_manager import (
    password_manager_view_model as view_model_module,
)


@pytest.fixture
def root() -> Iterator[tk.Tk]:
    try:
        window = tk.Tk()
    except tk.TclError:
        pytest.skip("no display available")
    window.withdraw()
    yield window
    window.destroy()


def test_save_then_search_through_window(
    root: tk.Tk, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    shown: list[str] = []
    monkeypatch.setattr(view_module.messagebox, "askokcancel", lambda **_: True)
    monkeypatch.setattr(
        view_module.messagebox, "showinfo", lambda **kw: shown.append(kw["message"])
    )
    repository = JsonPasswordRepository(tmp_path / "data.json")
    view = view_module.PasswordManagerView(
        root,
        view_model_module.PasswordManagerViewModel(
            SavePasswordEntry(repository),
            FindPasswordEntry(repository),
            GeneratePassword(),
        ),
    )
    view.website_entry.insert(0, "example.com")
    view.generate_password()
    password = view.password_entry.get()
    assert root.clipboard_get() == password

    view.save()

    assert view.website_entry.get() == ""
    assert view.password_entry.get() == ""
    view.website_entry.insert(0, "example.com")
    view.find_password()
    assert shown[-1] == constants.MESSAGE_DETAILS.format(
        email=constants.DEFAULT_EMAIL, password=password
    )
