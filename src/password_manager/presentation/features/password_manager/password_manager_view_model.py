"""@brief View model of the password manager screen (no tkinter here).

@file password_manager_view_model.py
"""

from collections.abc import Callable
from dataclasses import dataclass

from password_manager import constants
from password_manager.application.use_cases import (
    FindPasswordEntry,
    GeneratePassword,
    SavePasswordEntry,
)
from password_manager.domain.errors import (
    DataFileNotFoundError,
    EmptyFieldError,
    EntryNotFoundError,
    InvalidDataFileError,
)


@dataclass(frozen=True, slots=True)
class ActionResult:
    """@brief What the view shows after an action."""

    title: str  ##< Title of the message box.
    message: str  ##< Text of the message box.
    is_error: bool  ##< True when the box is a warning rather than information.
    clear_fields: bool = False  ##< True when the view clears website and password.


def _ignore_clipboard(text: str) -> None:
    """@brief Default clipboard: discards the text until the view binds one."""


def _decline_save(message: str) -> bool:
    """@brief Default confirmation: declines until the view binds a dialog."""
    return False


class PasswordManagerViewModel:
    """@brief Data and commands of the password manager screen."""

    def __init__(
        self,
        save_entry: SavePasswordEntry,
        find_entry: FindPasswordEntry,
        generate: GeneratePassword,
        copy_to_clipboard: Callable[[str], None] = _ignore_clipboard,
        confirm_save: Callable[[str], bool] = _decline_save,
    ) -> None:
        """@brief Create the view model.

        @param save_entry Use case that stores an entry.
        @param find_entry Use case that looks an entry up.
        @param generate Use case that generates a password.
        @param copy_to_clipboard Puts text on the clipboard.
        @param confirm_save Asks the user to confirm a save; True means ok.
        """
        self._save_entry = save_entry
        self._find_entry = find_entry
        self._generate = generate
        self._copy_to_clipboard = copy_to_clipboard
        self._confirm_save = confirm_save

    def bind_ui(
        self,
        copy_to_clipboard: Callable[[str], None],
        confirm_save: Callable[[str], bool],
    ) -> None:
        """@brief Hand the view's clipboard and confirmation dialog to the model.

        @param copy_to_clipboard Puts text on the clipboard.
        @param confirm_save Asks the user to confirm a save; True means ok.
        """
        self._copy_to_clipboard = copy_to_clipboard
        self._confirm_save = confirm_save

    def generate_password(self) -> str:
        """@brief Generate a password and copy it to the clipboard.

        @return The generated password.
        """
        password = self._generate.execute()
        self._copy_to_clipboard(password)
        return password

    def save(self, website: str, email: str, password: str) -> ActionResult | None:
        """@brief Confirm and store the entry.

        @param website Website field.
        @param email E-mail field.
        @param password Password field.
        @return A result to show, or None when the user cancelled.
        """
        if not (website.strip() and email.strip() and password.strip()):
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_EMPTY_FIELDS, True
            )
        question = constants.MESSAGE_CONFIRM_SAVE.format(email=email, password=password)
        if not self._confirm_save(question):
            return None
        try:
            self._save_entry.execute(website, email, password)
        except EmptyFieldError:
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_EMPTY_FIELDS, True
            )
        except InvalidDataFileError:
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_INVALID_DATA_FILE, True
            )
        else:
            return ActionResult(
                constants.TITLE_SAVED,
                constants.MESSAGE_SAVED.format(website=website.strip()),
                False,
                clear_fields=True,
            )

    def find_password(self, website: str) -> ActionResult:
        """@brief Look up the credentials of a website.

        @param website Website field.
        @return The result to show.
        """
        try:
            entry = self._find_entry.execute(website)
        except EmptyFieldError:
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_EMPTY_FIELDS, True
            )
        except DataFileNotFoundError:
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_NO_DATA_FILE, True
            )
        except EntryNotFoundError as error:
            return ActionResult(
                constants.TITLE_OOPS,
                constants.MESSAGE_NO_DETAILS.format(website=error.website),
                True,
            )
        except InvalidDataFileError:
            return ActionResult(
                constants.TITLE_OOPS, constants.MESSAGE_INVALID_DATA_FILE, True
            )
        return ActionResult(
            entry.website,
            constants.MESSAGE_DETAILS.format(
                email=entry.email, password=entry.password
            ),
            False,
        )
