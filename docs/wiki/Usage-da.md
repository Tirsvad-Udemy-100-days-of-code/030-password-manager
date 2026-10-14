[English](Usage) · **Dansk** · [Bahasa Malaysia](Usage-ms)

# Brug

Start programmet med det virtuelle miljø aktivt:

```bash
python -m password_manager
```

Programmet gemmer sine data i `data.json` i den mappe, du starter det fra.

## Generér og tilføj en adgangskode

1. Skriv webstedet.
2. Tryk på **Generate Password**. En adgangskode indsættes og kopieres til
   udklipsholderen.
3. Kontrollér e-mailadressen og tryk på **Add**. Bekræft dialogen, så gemmes
   posten.

![Hovedvinduet efter Generate Password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/main-window.png)

![Bekræftelsen før en post gemmes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/add-confirmation.png)

Hvis et felt er tomt, vises en advarsel, og intet gemmes.

## Søg

Skriv et websted og tryk på **Search**. Den gemte e-mailadresse og adgangskode
vises.

![Søgningen finder et gemt websted](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-found.png)

Hvis der ikke er gemt noget for webstedet, eller datafilen endnu ikke findes,
fortæller en besked det.

![Søgning efter et ukendt websted](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-not-found.png)

## Datafilen

`data.json` indeholder én post pr. websted:

```json
{
    "example.com": {
        "email": "jens@example.com",
        "password": "Sample#Pass123"
    }
}
```
