[English](Usage) · [Dansk](Usage-da) · **Bahasa Malaysia**

# Penggunaan

Mulakan program dengan persekitaran maya aktif:

```bash
python -m password_manager
```

Program menyimpan datanya dalam `data.json` di folder tempat anda memulakannya.

## Jana dan tambah kata laluan

1. Taip laman web.
2. Tekan **Generate Password**. Kata laluan diisi dan disalin ke papan
   keratan.
3. Semak alamat e-mel dan tekan **Add**. Sahkan dialog dan rekod disimpan.

![Tetingkap utama selepas Generate Password](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/main-window.png)

![Pengesahan sebelum rekod disimpan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/add-confirmation.png)

Jika medan dibiarkan kosong, amaran dipaparkan dan tiada apa yang disimpan.

## Carian

Taip laman web dan tekan **Search**. Alamat e-mel dan kata laluan yang disimpan
dipaparkan.

![Carian menemui laman web yang disimpan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-found.png)

Jika tiada apa yang disimpan untuk laman web itu, atau fail data belum wujud,
satu mesej memberitahunya.

![Carian untuk laman web yang tidak dikenali](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/raw/branch/main/docs/images/search-not-found.png)

## Fail data

`data.json` mengandungi satu rekod bagi setiap laman web:

```json
{
    "example.com": {
        "email": "jens@example.com",
        "password": "Sample#Pass123"
    }
}
```
