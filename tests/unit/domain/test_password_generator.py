import random

from password_manager import constants
from password_manager.domain.password_generator import generate_password


def _count(password: str, alphabet: str) -> int:
    return sum(1 for char in password if char in alphabet)


def test_generate_password_length_within_bounds() -> None:
    low = constants.MIN_LETTERS + constants.MIN_SYMBOLS + constants.MIN_DIGITS
    high = constants.MAX_LETTERS + constants.MAX_SYMBOLS + constants.MAX_DIGITS
    for seed in range(50):
        assert low <= len(generate_password(random.Random(seed))) <= high


def test_generate_password_uses_all_three_classes_within_bounds() -> None:
    for seed in range(50):
        password = generate_password(random.Random(seed))
        letters = _count(password, constants.LETTERS)
        symbols = _count(password, constants.SYMBOLS)
        digits = _count(password, constants.DIGITS)
        assert constants.MIN_LETTERS <= letters <= constants.MAX_LETTERS
        assert constants.MIN_SYMBOLS <= symbols <= constants.MAX_SYMBOLS
        assert constants.MIN_DIGITS <= digits <= constants.MAX_DIGITS
        assert letters + symbols + digits == len(password)


def test_generate_password_is_reproducible_with_same_seed() -> None:
    assert generate_password(random.Random(7)) == generate_password(random.Random(7))


def test_generate_password_default_source_works() -> None:
    assert generate_password()
