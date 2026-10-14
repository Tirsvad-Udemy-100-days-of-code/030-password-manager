"""@brief Password repository that keeps entries in a JSON file.

@file json_password_repository.py
"""

import json
from pathlib import Path
from typing import Any

from password_manager import constants
from password_manager.domain.errors import (
    DataFileNotFoundError,
    EntryNotFoundError,
    InvalidDataFileError,
)
from password_manager.domain.password_entry import PasswordEntry


class JsonPasswordRepository:
    """@brief Stores entries as {website: {"email": ..., "password": ...}}."""

    def __init__(self, path: Path) -> None:
        """@brief Create the repository.

        @param path Location of the JSON file.
        """
        self._path = path

    def add(self, entry: PasswordEntry) -> None:
        """@brief Store an entry; a missing or empty file is created or rewritten.

        @param entry The entry to store.
        @throws InvalidDataFileError The file holds JSON that is not an object.
        """
        try:
            data = self._load()
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data[entry.website] = {
            constants.KEY_EMAIL: entry.email,
            constants.KEY_PASSWORD: entry.password,
        }
        with self._path.open("w", encoding=constants.FILE_ENCODING, newline="\n") as f:
            json.dump(data, f, indent=constants.JSON_INDENT)

    def find(self, website: str) -> PasswordEntry:
        """@brief Look an entry up.

        @param website Website to look for.
        @return The stored entry.
        @throws DataFileNotFoundError The file does not exist.
        @throws EntryNotFoundError The website has no entry (or the file is empty).
        @throws InvalidDataFileError The file has an unexpected structure.
        """
        try:
            data = self._load()
        except FileNotFoundError as error:
            raise DataFileNotFoundError from error
        except json.JSONDecodeError as error:
            raise EntryNotFoundError(website) from error
        if website not in data:
            raise EntryNotFoundError(website)
        details = data[website]
        try:
            return PasswordEntry(
                website,
                details[constants.KEY_EMAIL],
                details[constants.KEY_PASSWORD],
            )
        except (KeyError, TypeError) as error:
            raise InvalidDataFileError from error

    # Any: the values of a JSON object are unchecked until `find` validates them.
    def _load(self) -> dict[str, Any]:
        with self._path.open("r", encoding=constants.FILE_ENCODING) as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise InvalidDataFileError
        return data
