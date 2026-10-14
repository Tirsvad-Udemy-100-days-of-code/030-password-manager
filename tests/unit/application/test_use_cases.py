import random

import pytest
from conftest import FakePasswordRepository

from password_manager.application.use_cases import (
    FindPasswordEntry,
    GeneratePassword,
    SavePasswordEntry,
)
from password_manager.domain.errors import (
    DataFileNotFoundError,
    EmptyFieldError,
    EntryNotFoundError,
)
from password_manager.domain.password_entry import PasswordEntry


def test_save_stores_entry(repository: FakePasswordRepository) -> None:
    SavePasswordEntry(repository).execute("example.com", "me@x.org", "pw")

    assert repository.entries["example.com"] == PasswordEntry(
        "example.com", "me@x.org", "pw"
    )


@pytest.mark.parametrize(
    ("website", "email", "password"),
    [("", "e", "p"), ("w", "", "p"), ("w", "e", ""), ("  ", "e", "p")],
)
def test_save_rejects_empty_field(
    repository: FakePasswordRepository, website: str, email: str, password: str
) -> None:
    with pytest.raises(EmptyFieldError):
        SavePasswordEntry(repository).execute(website, email, password)
    assert repository.entries == {}


def test_find_returns_entry(repository: FakePasswordRepository) -> None:
    SavePasswordEntry(repository).execute("example.com", "me@x.org", "pw")

    entry = FindPasswordEntry(repository).execute("example.com")

    assert entry.email == "me@x.org"


def test_find_raises_when_website_unknown(
    repository: FakePasswordRepository,
) -> None:
    with pytest.raises(EntryNotFoundError):
        FindPasswordEntry(repository).execute("nope.com")


def test_find_raises_when_no_data_file() -> None:
    with pytest.raises(DataFileNotFoundError):
        FindPasswordEntry(FakePasswordRepository(has_file=False)).execute("a.com")


def test_find_rejects_empty_website(repository: FakePasswordRepository) -> None:
    with pytest.raises(EmptyFieldError):
        FindPasswordEntry(repository).execute("")


def test_generate_uses_given_random_source() -> None:
    first = GeneratePassword(random.Random(1)).execute()
    second = GeneratePassword(random.Random(1)).execute()

    assert first == second
