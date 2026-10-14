"""@brief The password entry of the domain.

@file password_entry.py
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PasswordEntry:
    """@brief The credentials stored for one website."""

    website: str  ##< The website the credentials belong to.
    email: str  ##< E-mail address or user name.
    password: str  ##< The password.
