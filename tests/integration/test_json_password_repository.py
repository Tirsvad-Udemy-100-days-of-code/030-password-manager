import json
from pathlib import Path

import pytest

from password_manager.domain.errors import (
    DataFileNotFoundError,
    EntryNotFoundError,
    InvalidDataFileError,
)
from password_manager.domain.password_entry import PasswordEntry
from password_manager.infrastructure.persistence.json_password_repository import (
    JsonPasswordRepository,
)

ENTRY = PasswordEntry("example.com", "me@x.org", "pw1")


def test_add_writes_nested_json_and_reads_back(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    repository = JsonPasswordRepository(path)

    repository.add(ENTRY)

    assert json.loads(path.read_text("utf-8")) == {
        "example.com": {"email": "me@x.org", "password": "pw1"}
    }
    assert repository.find("example.com") == ENTRY


def test_add_uses_indent_of_four(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    JsonPasswordRepository(path).add(ENTRY)

    assert '\n    "example.com"' in path.read_text("utf-8")


def test_add_keeps_existing_entries(tmp_path: Path) -> None:
    repository = JsonPasswordRepository(tmp_path / "data.json")
    other = PasswordEntry("other.org", "o@x.org", "pw2")
    repository.add(ENTRY)

    repository.add(other)

    assert repository.find("example.com") == ENTRY
    assert repository.find("other.org") == other


def test_add_creates_missing_file(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    assert not path.exists()

    JsonPasswordRepository(path).add(ENTRY)

    assert path.exists()


def test_add_rewrites_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text("", encoding="utf-8")

    JsonPasswordRepository(path).add(ENTRY)

    assert JsonPasswordRepository(path).find("example.com") == ENTRY


def test_add_rewrites_invalid_json(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text("{not json", encoding="utf-8")

    JsonPasswordRepository(path).add(ENTRY)

    assert JsonPasswordRepository(path).find("example.com") == ENTRY


def test_add_refuses_json_that_is_not_an_object(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text("[1, 2]", encoding="utf-8")

    with pytest.raises(InvalidDataFileError):
        JsonPasswordRepository(path).add(ENTRY)
    assert path.read_text("utf-8") == "[1, 2]"


def test_find_raises_when_file_missing(tmp_path: Path) -> None:
    with pytest.raises(DataFileNotFoundError):
        JsonPasswordRepository(tmp_path / "data.json").find("example.com")


def test_find_raises_when_website_absent(tmp_path: Path) -> None:
    repository = JsonPasswordRepository(tmp_path / "data.json")
    repository.add(ENTRY)

    with pytest.raises(EntryNotFoundError):
        repository.find("nope.com")


def test_find_raises_not_found_on_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text("", encoding="utf-8")

    with pytest.raises(EntryNotFoundError):
        JsonPasswordRepository(path).find("example.com")


def test_find_raises_when_entry_lacks_keys(tmp_path: Path) -> None:
    path = tmp_path / "data.json"
    path.write_text('{"example.com": {"email": "e"}}', encoding="utf-8")

    with pytest.raises(InvalidDataFileError):
        JsonPasswordRepository(path).find("example.com")
