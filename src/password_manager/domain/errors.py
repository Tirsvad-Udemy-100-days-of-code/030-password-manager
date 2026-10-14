"""@brief Errors raised by the business rules of the password manager.

@file errors.py
"""


class PasswordManagerError(Exception):
    """@brief Base class of every error the password manager raises on purpose."""


class EmptyFieldError(PasswordManagerError):
    """@brief A required field was left empty."""


class DataFileNotFoundError(PasswordManagerError):
    """@brief The data file does not exist, so nothing can be looked up."""


class InvalidDataFileError(PasswordManagerError):
    """@brief The data file exists but does not hold the expected structure."""


class EntryNotFoundError(PasswordManagerError):
    """@brief No entry is stored for a website."""

    def __init__(self, website: str) -> None:
        """@brief Create the error.

        @param website The website that was looked up.
        """
        super().__init__(website)
        self.website = website
