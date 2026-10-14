"""Smoke test: the package and its constants import and hold sane values."""

import password_manager
from password_manager import constants


def test_package_has_version() -> None:
    assert password_manager.__version__


def test_data_file_name_is_json() -> None:
    assert constants.DATA_FILE_NAME.endswith(".json")


def test_password_length_bounds_are_ordered() -> None:
    assert constants.MIN_LETTERS <= constants.MAX_LETTERS
    assert constants.MIN_SYMBOLS <= constants.MAX_SYMBOLS
    assert constants.MIN_DIGITS <= constants.MAX_DIGITS
