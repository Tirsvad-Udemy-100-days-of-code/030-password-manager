"""Shared fakes of the ports for the unit tests."""

import pytest

from password_manager.domain.errors import DataFileNotFoundError, EntryNotFoundError
from password_manager.domain.password_entry import PasswordEntry


class FakePasswordRepository:
    """In-memory PasswordRepository; `has_file` False mimics a missing file."""

    def __init__(self, has_file: bool = True) -> None:
        self.entries: dict[str, PasswordEntry] = {}
        self.has_file = has_file

    def add(self, entry: PasswordEntry) -> None:
        self.entries[entry.website] = entry
        self.has_file = True

    def find(self, website: str) -> PasswordEntry:
        if not self.has_file:
            raise DataFileNotFoundError
        if website not in self.entries:
            raise EntryNotFoundError(website)
        return self.entries[website]


@pytest.fixture
def repository() -> FakePasswordRepository:
    return FakePasswordRepository()
