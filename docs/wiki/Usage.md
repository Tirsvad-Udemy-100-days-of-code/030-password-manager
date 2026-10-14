**English** · [Dansk](Usage-da) · [Bahasa Malaysia](Usage-ms)

# Usage

Start the program with the virtual environment active:

```bash
python -m password_manager
```

The program keeps its data in `data.json` in the folder you start it from.

## Generate and add a password

1. Type the website.
2. Press **Generate Password**. A password is filled in and copied to the
   clipboard.
3. Check the e-mail address and press **Add**. Confirm the dialog and the entry
   is saved.

![The main window after Generate Password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/main-window.png)

![The confirmation before an entry is saved](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/add-confirmation.png)

Leaving a field empty shows a warning and saves nothing.

## Search

Type a website and press **Search**. The saved e-mail address and password are
shown.

![Search finds a saved website](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-found.png)

If nothing is saved for the website, or no data file exists yet, a message says
so.

![Search for an unknown website](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-not-found.png)

## The data file

`data.json` holds one record per website:

```json
{
    "example.com": {
        "email": "jens@example.com",
        "password": "Sample#Pass123"
    }
}
```
