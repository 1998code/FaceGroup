# Pengelompok Wajah (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Alat ini secara otomatis mengenali wajah dalam gambar dan mengelompokkannya ke dalam folder.

## Persyaratan

- **Sistem Operasi:** macOS, Linux, atau Windows
- **Versi Python:** `3.11.9` (ditentukan dalam `.python-version`)
- **Pustaka Utama:** `face_recognition`, `opencv-python`, `numpy`

## Pengaturan

1. Instal dependensi:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Tempatkan gambar Anda dalam folder bernama `input_images`.

3. Jalankan skrip:
   ```bash
   python face_grouper.py
   ```

## Cara Kerja

Skrip akan:
1. Memindai semua gambar di direktori `input_images`.
2. Mendeteksi wajah dan menghasilkan tanda tangan unik untuk setiap orang.
3. Membuat folder untuk setiap orang yang terdeteksi di `output_groups`.
4. Menyalin gambar ke folder yang sesuai.

*Catatan: Jika sebuah gambar berisi beberapa orang, gambar tersebut akan disalin ke folder masing-masing orang yang terdeteksi.*
