"""@brief Use cases of the password manager.

@file use_cases.py
"""

import random

from password_manager.application.ports import PasswordRepository
from password_manager.domain.errors import EmptyFieldError
from password_manager.domain.password_entry import PasswordEntry
from password_manager.domain.password_generator import generate_password


class SavePasswordEntry:
    """@brief Validate and store a password entry."""

    def __init__(self, repository: PasswordRepository) -> None:
        """@brief Create the use case.

        @param repository Where entries are stored.
        """
        self._repository = repository

    def execute(self, website: str, email: str, password: str) -> None:
        """@brief Store the entry.

        @param website Website of the entry.
        @param email E-mail address or user name.
        @param password The password.
        @throws EmptyFieldError A field is empty.
        """
        if not (website.strip() and email.strip() and password.strip()):
            raise EmptyFieldError
        self._repository.add(PasswordEntry(website.strip(), email, password))


class FindPasswordEntry:
    """@brief Look up the entry of a website."""

    def __init__(self, repository: PasswordRepository) -> None:
        """@brief Create the use case.

        @param repository Where entries are stored.
        """
        self._repository = repository

    def execute(self, website: str) -> PasswordEntry:
        """@brief Find the entry.

        @param website Website to look for.
        @return The stored entry.
        @throws EmptyFieldError The website is empty.
        @throws DataFileNotFoundError There is no storage yet.
        @throws EntryNotFoundError The website has no entry.
        """
        if not website.strip():
            raise EmptyFieldError
        return self._repository.find(website.strip())


class GeneratePassword:
    """@brief Produce a new random password."""

    def __init__(self, rng: random.Random | None = None) -> None:
        """@brief Create the use case.

        @param rng Random source; secure by default.
        """
        self._rng = rng

    def execute(self) -> str:
        """@brief Generate a password.

        @return The new password.
        """
        return generate_password(self._rng)
