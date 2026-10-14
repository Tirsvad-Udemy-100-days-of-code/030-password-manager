**English** · [Dansk](Installation-da) · [Bahasa Malaysia](Installation-ms)

# Installation

## Requirements

- Python 3.13 or newer with Tkinter. On Debian or Ubuntu install `python3-tk`.
- `venv` and `pip`, both part of Python.
- No runtime dependencies.

## Create a local virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The `[dev]` extra installs pytest and ruff. Leave it out
(`python -m pip install -e .`) if you only want to run the program.

## Check the installation

```bash
python -m pytest
```
