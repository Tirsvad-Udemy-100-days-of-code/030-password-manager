"""@brief Generation of random passwords.

@file password_generator.py
"""

import random

from password_manager import constants


def generate_password(rng: random.Random | None = None) -> str:
    """@brief Build a shuffled password of letters, symbols and digits.

    @param rng Random source; a cryptographically secure one when omitted.
    @return The generated password; each class count is within its bounds.
    """
    source = rng if rng is not None else random.SystemRandom()
    characters = (
        _pick(source, constants.LETTERS, constants.MIN_LETTERS, constants.MAX_LETTERS)
        + _pick(source, constants.SYMBOLS, constants.MIN_SYMBOLS, constants.MAX_SYMBOLS)
        + _pick(source, constants.DIGITS, constants.MIN_DIGITS, constants.MAX_DIGITS)
    )
    source.shuffle(characters)
    return "".join(characters)


def _pick(source: random.Random, alphabet: str, low: int, high: int) -> list[str]:
    count = source.randint(low, high)
    return [source.choice(alphabet) for _ in range(count)]
