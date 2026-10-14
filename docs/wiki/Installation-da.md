[English](Installation) · **Dansk** · [Bahasa Malaysia](Installation-ms)

# Installation

## Krav

- Python 3.13 eller nyere med Tkinter. På Debian eller Ubuntu installeres
  `python3-tk`.
- `venv` og `pip`, som begge er en del af Python.
- Ingen afhængigheder i drift.

## Opret et lokalt virtuelt miljø

Windows (PowerShell):

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Tillægget `[dev]` installerer pytest og ruff. Udelad det
(`python -m pip install -e .`), hvis du kun vil køre programmet.

## Kontrollér installationen

```bash
python -m pytest
```
