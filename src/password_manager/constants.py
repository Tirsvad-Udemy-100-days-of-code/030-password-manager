"""@brief Constants of the password manager.

@file constants.py
@details Every literal that more than one module needs, or that a reader may
want to change, lives here and nowhere else.
"""

import string
from pathlib import Path

# Storage
DATA_FILE_NAME = "data.json"  ##< Name of the JSON file that holds the entries.
DATA_FILE_PATH = Path(
    DATA_FILE_NAME
)  ##< Default location, relative to the working directory.
JSON_INDENT = 4  ##< Indentation of the written JSON, for readability.
KEY_EMAIL = "email"  ##< JSON key of an entry's e-mail address.
KEY_PASSWORD = "password"  ##< JSON key of an entry's password.
FILE_ENCODING = "utf-8"  ##< Text encoding of the data file.

# Password generator
LETTERS = string.ascii_letters  ##< Letters a password may use.
DIGITS = string.digits  ##< Digits a password may use.
SYMBOLS = "!#$%&()*+"  ##< Symbols a password may use.
MIN_LETTERS = 8  ##< Fewest letters in a generated password.
MAX_LETTERS = 10  ##< Most letters in a generated password.
MIN_SYMBOLS = 2  ##< Fewest symbols in a generated password.
MAX_SYMBOLS = 4  ##< Most symbols in a generated password.
MIN_DIGITS = 2  ##< Fewest digits in a generated password.
MAX_DIGITS = 4  ##< Most digits in a generated password.

# Window
WINDOW_TITLE = "Password Manager"  ##< Title of the main window.
WINDOW_PADDING = 50  ##< Padding around the window content, in pixels.
LOGO_SIZE = 200  ##< Width and height of the logo canvas, in pixels.
DEFAULT_EMAIL = "name@example.com"  ##< E-mail address the form starts with.
ENTRY_WIDTH_WIDE = 35  ##< Width in characters of the e-mail and add fields.
ENTRY_WIDTH_NARROW = 21  ##< Width in characters of the website and password fields.

# Logo (a padlock drawn with canvas shapes)
LOGO_BACKGROUND = "white"  ##< Canvas background colour.
LOGO_BODY_COLOR = "#2b6cb0"  ##< Fill of the padlock body.
LOGO_SHACKLE_COLOR = "#4a5568"  ##< Outline colour of the padlock shackle.
LOGO_KEYHOLE_COLOR = "white"  ##< Fill of the keyhole.
LOGO_SHACKLE_WIDTH = 12  ##< Line width of the shackle, in pixels.
LOGO_BODY_BOX = (50, 100, 150, 180)  ##< Padlock body rectangle (x0, y0, x1, y1).
LOGO_SHACKLE_BOX = (65, 30, 135, 170)  ##< Bounding box of the shackle arc.
LOGO_KEYHOLE_BOX = (92, 125, 108, 141)  ##< Bounding box of the keyhole circle.
LOGO_KEYHOLE_SLOT = (97, 138, 103, 160)  ##< Rectangle of the keyhole slot.

# Labels and messages
LABEL_WEBSITE = "Website:"
LABEL_EMAIL = "Email/Username:"
LABEL_PASSWORD = "Password:"
BUTTON_SEARCH = "Search"
BUTTON_GENERATE = "Generate Password"
BUTTON_ADD = "Add"
TITLE_OOPS = "Oops"
TITLE_SAVED = "Saved"
TITLE_FOUND = "Found"
MESSAGE_EMPTY_FIELDS = "Please don't leave any fields empty!"
MESSAGE_NO_DATA_FILE = "No Data File Found."
MESSAGE_NO_DETAILS = "No details for {website} exists."
MESSAGE_CONFIRM_SAVE = (
    "These are the details entered:\nEmail: {email}\n"
    "Password: {password}\nIs it ok to save?"
)
MESSAGE_DETAILS = "Email: {email}\nPassword: {password}"
MESSAGE_INVALID_DATA_FILE = "The data file has an unexpected format."
MESSAGE_SAVED = "Details for {website} were saved."
