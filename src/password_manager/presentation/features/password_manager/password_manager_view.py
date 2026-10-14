"""@brief Tkinter view of the password manager screen.

@file password_manager_view.py
"""

import tkinter as tk
from tkinter import messagebox

from password_manager import constants
from password_manager.presentation.features.password_manager import (
    password_manager_view_model as view_model_module,
)


class PasswordManagerView:
    """@brief The window: shows the fields and raises events to the view model."""

    def __init__(
        self, root: tk.Tk, view_model: view_model_module.PasswordManagerViewModel
    ) -> None:
        """@brief Build the widgets on a root window.

        @param root The Tk root window.
        @param view_model The view model the events are forwarded to.
        """
        self._root = root
        self._view_model = view_model
        self._view_model.bind_ui(self._copy_to_clipboard, self._confirm_save)
        root.title(constants.WINDOW_TITLE)
        root.config(padx=constants.WINDOW_PADDING, pady=constants.WINDOW_PADDING)
        self._build_logo()
        self._build_form()

    @property
    def website_entry(self) -> tk.Entry:
        """@return The website input."""
        return self._website_entry

    @property
    def email_entry(self) -> tk.Entry:
        """@return The e-mail input."""
        return self._email_entry

    @property
    def password_entry(self) -> tk.Entry:
        """@return The password input."""
        return self._password_entry

    def generate_password(self) -> None:
        """@brief Fill the password field with a new password (and copy it)."""
        password = self._view_model.generate_password()
        self._password_entry.delete(0, tk.END)
        self._password_entry.insert(0, password)

    def save(self) -> None:
        """@brief Ask the view model to store the entered details."""
        result = self._view_model.save(
            self._website_entry.get(),
            self._email_entry.get(),
            self._password_entry.get(),
        )
        if result is None:
            return
        self._show(result)
        if result.clear_fields:
            self._clear_fields()

    def find_password(self) -> None:
        """@brief Show the stored details of the entered website."""
        self._show(self._view_model.find_password(self._website_entry.get()))

    def _build_logo(self) -> None:
        size = constants.LOGO_SIZE
        canvas = tk.Canvas(
            self._root,
            width=size,
            height=size,
            bg=constants.LOGO_BACKGROUND,
            highlightthickness=0,
        )
        canvas.create_arc(
            *constants.LOGO_SHACKLE_BOX,
            start=0,
            extent=180,
            style=tk.ARC,
            outline=constants.LOGO_SHACKLE_COLOR,
            width=constants.LOGO_SHACKLE_WIDTH,
        )
        canvas.create_rectangle(
            *constants.LOGO_BODY_BOX,
            fill=constants.LOGO_BODY_COLOR,
            outline=constants.LOGO_BODY_COLOR,
        )
        canvas.create_oval(
            *constants.LOGO_KEYHOLE_BOX,
            fill=constants.LOGO_KEYHOLE_COLOR,
            outline=constants.LOGO_KEYHOLE_COLOR,
        )
        canvas.create_rectangle(
            *constants.LOGO_KEYHOLE_SLOT,
            fill=constants.LOGO_KEYHOLE_COLOR,
            outline=constants.LOGO_KEYHOLE_COLOR,
        )
        canvas.grid(row=0, column=1)

    def _build_form(self) -> None:
        root = self._root
        tk.Label(root, text=constants.LABEL_WEBSITE).grid(row=1, column=0)
        tk.Label(root, text=constants.LABEL_EMAIL).grid(row=2, column=0)
        tk.Label(root, text=constants.LABEL_PASSWORD).grid(row=3, column=0)

        self._website_entry = tk.Entry(root, width=constants.ENTRY_WIDTH_NARROW)
        self._website_entry.grid(row=1, column=1, sticky="EW")
        self._website_entry.focus()
        self._email_entry = tk.Entry(root, width=constants.ENTRY_WIDTH_WIDE)
        self._email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
        self._email_entry.insert(0, constants.DEFAULT_EMAIL)
        self._password_entry = tk.Entry(root, width=constants.ENTRY_WIDTH_NARROW)
        self._password_entry.grid(row=3, column=1, sticky="EW")

        self._search_button = tk.Button(
            root, text=constants.BUTTON_SEARCH, command=self.find_password
        )
        self._search_button.grid(row=1, column=2, sticky="EW")
        self._generate_button = tk.Button(
            root, text=constants.BUTTON_GENERATE, command=self.generate_password
        )
        self._generate_button.grid(row=3, column=2, sticky="EW")
        self._add_button = tk.Button(
            root,
            text=constants.BUTTON_ADD,
            width=constants.ENTRY_WIDTH_WIDE,
            command=self.save,
        )
        self._add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

    def _copy_to_clipboard(self, text: str) -> None:
        self._root.clipboard_clear()
        self._root.clipboard_append(text)

    @staticmethod
    def _confirm_save(message: str) -> bool:
        return bool(
            messagebox.askokcancel(title=constants.WINDOW_TITLE, message=message)
        )

    @staticmethod
    def _show(result: view_model_module.ActionResult) -> None:
        if result.is_error:
            messagebox.showwarning(title=result.title, message=result.message)
        else:
            messagebox.showinfo(title=result.title, message=result.message)

    def _clear_fields(self) -> None:
        self._website_entry.delete(0, tk.END)
        self._password_entry.delete(0, tk.END)
