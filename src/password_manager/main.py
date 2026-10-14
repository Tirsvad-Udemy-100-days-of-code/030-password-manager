"""@brief Composition root: wires the layers together and runs the window.

@file main.py
"""

import tkinter as tk

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


def main() -> None:
    """@brief Build the application and run the Tk main loop."""
    repository = JsonPasswordRepository(constants.DATA_FILE_PATH)
    view_model = view_model_module.PasswordManagerViewModel(
        SavePasswordEntry(repository),
        FindPasswordEntry(repository),
        GeneratePassword(),
    )
    root = tk.Tk()
    view_module.PasswordManagerView(root, view_model)
    root.mainloop()


if __name__ == "__main__":
    main()
