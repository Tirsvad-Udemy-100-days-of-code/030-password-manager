[English](Development) · [Dansk](Development-da) · **Bahasa Malaysia**

# Pembangunan

## Susun atur

| Folder | Kandungan |
| --- | --- |
| `src/password_manager/domain` | Rekod, penjana kata laluan dan ralat; tiada input atau output |
| `src/password_manager/application` | Kes guna dan port repositori |
| `src/password_manager/infrastructure` | Repositori JSON |
| `src/password_manager/presentation` | Paparan MVVM dan model paparan |
| `src/password_manager/constants.py` | Semua pemalar dan mesej |
| `tests/` | Ujian `unit`, `integration` dan `e2e` |
| `tools/` | `capture_screenshots.py` |

Import menuju ke dalam; hanya `main.py` menghubungkan lapisan.

## Ujian dan lint

```bash
python -m pytest
python -m ruff format src tests tools
python -m ruff check src tests tools
```

## Dokumentasi kod sumber

Komen ditulis dalam gaya Doxygen. Bina HTML dengan `doxygen Doxyfile`; ia dibuka
di `docs/doxygen/html/index.html`.

## Tangkapan skrin

Pada Windows dengan persekitaran maya aktif:

```bash
python tools/capture_screenshots.py
```

Imej ditulis ke `docs/images/` daripada tetingkap sebenar dan fail data
sementara.

## Dokumen projek

Projek mengikut aliran kerja perancangan dahulu: Business Case, analisis
pemegang taruh, pelan projek dan pencapaian berada dalam `docs/`. Kerja
dilakukan pada satu cabang dan satu pull request bagi setiap pencapaian.
