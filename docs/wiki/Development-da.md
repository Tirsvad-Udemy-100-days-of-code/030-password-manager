[English](Development) · **Dansk** · [Bahasa Malaysia](Development-ms)

# Udvikling

## Opbygning

| Mappe | Indhold |
| --- | --- |
| `src/password_manager/domain` | Post, adgangskodegenerator og fejl; ingen ind- eller udlæsning |
| `src/password_manager/application` | Use cases og lagerporten |
| `src/password_manager/infrastructure` | JSON-lageret |
| `src/password_manager/presentation` | MVVM-visningen og visningsmodellen |
| `src/password_manager/constants.py` | Alle konstanter og beskeder |
| `tests/` | `unit`-, `integration`- og `e2e`-tests |
| `tools/` | `capture_screenshots.py` |

Importer peger indad; kun `main.py` forbinder lagene.

## Tests og lint

```bash
python -m pytest
python -m ruff format src tests tools
python -m ruff check src tests tools
```

## Kildedokumentation

Kommentarerne er i Doxygen-stil. Byg HTML med `doxygen Doxyfile`; den åbnes på
`docs/doxygen/html/index.html`.

## Skærmbilleder

På Windows med det virtuelle miljø aktivt:

```bash
python tools/capture_screenshots.py
```

Billederne skrives til `docs/images/` fra det rigtige vindue og en midlertidig
datafil.

## Projektdokumenter

Projektet følger en planlæg-først-arbejdsgang: Business Case, interessentanalyse,
projektplan og milepæle ligger i `docs/`. Arbejdet udføres på én gren og én pull
request pr. milepæl.
