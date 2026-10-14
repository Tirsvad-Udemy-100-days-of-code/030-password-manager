"""@brief Ports the use cases need from the outside.

@file ports.py
"""

from typing import Protocol

from password_manager.domain.password_entry import PasswordEntry


class PasswordRepository(Protocol):
    """@brief Storage of password entries."""

    def add(self, entry: PasswordEntry) -> None:
        """@brief Store an entry, keeping every other entry.

        @param entry The entry to store; replaces one for the same website.
        @throws InvalidDataFileError The stored data has an unexpected format.
        """
        ...

    def find(self, website: str) -> PasswordEntry:
        """@brief Look an entry up.

        @param website The website to look for.
        @return The stored entry.
        @throws DataFileNotFoundError There is no storage yet.
        @throws EntryNotFoundError The website has no entry.
        @throws InvalidDataFileError The stored data has an unexpected format.
        """
        ...
