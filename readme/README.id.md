# Pengelompok Wajah (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

Alat ini secara otomatis mengenali wajah dalam gambar dan mengelompokkannya ke dalam folder.

## Persyaratan

- **Sistem Operasi:** macOS, Linux, atau Windows
- **Versi Python:** `3.11.9` (ditentukan dalam `.python-version`)
- **Pustaka Utama:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## Instalasi & Eksekusi

### 1. Instalasi
Pertama, pastikan Anda telah menyiapkan lingkungan virtual dan menginstal semua dependensi.

#### macOS / Linux:
```bash
# Buat dan aktifkan lingkungan virtual
python3 -m venv venv
source venv/bin/activate

# Instal persyaratan
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# Buat dan aktifkan lingkungan virtual
python -m venv venv
.\venv\Scripts\activate

# Instal persyaratan
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Menjalankan Alat
Kami merekomendasikan penggunaan antarmuka web modern untuk pengalaman terbaik.

#### Luncurkan GUI Web (Direkomendasikan):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

![Face Grouper GUI](../GUI.png)

#### Luncurkan Versi CLI:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## Troubleshooting

### `ModuleNotFoundError: No module named 'face_recognition'`
Ini biasanya terjadi saat Anda menjalankan skrip di luar lingkungan virtual. Selalu pastikan untuk menggunakan jalur ke python lingkungan virtual:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
Di macOS, gunakan `python3` daripada `python`.

### Pemrosesan sangat lambat
Pengenalan wajah sangat intensif CPU. Menutup aplikasi berat lainnya atau menggunakan mesin dengan lebih banyak core akan membantu.

### Hasil deteksi buruk
Coba sesuaikan slider **Tolerance (Strictness)** di UI:
- **Lebih Rendah (misal: 0.4):** Lebih ketat. Gunakan ini jika alat mencampur orang yang berbeda ke dalam satu folder.
- **Lebih Tinggi (misal: 0.6):** Lebih longgar. Gunakan ini jika alat membuat terlalu banyak folder untuk orang yang sama.

## Kontribusi

Kontribusi sangat disambut! Jika Anda ingin membantu meningkatkan alat ini, harap:
1. Fork repositori ini.
2. Buat cabang baru untuk fitur atau perbaikan bug Anda.
3. Kirimkan pull request dengan deskripsi jelas tentang perubahan Anda.

## Cara Kerja

1. **Scan**: Memindai semua gambar di direktori input yang Anda tentukan.
2. **Detect**: Menggunakan AI untuk mendeteksi wajah dan menghasilkan tanda tangan unik.
3. **Group**: Mengelompokkan wajah serupa berdasarkan tingkat ketatnya preferensi Anda.
4. **Organize**: Membuat folder di direktori output dan menyalin gambar ke dalamnya.
5. **UI**: Menampilkan galeri real-time dari orang unik yang terdeteksi.

*Catatan: Jika sebuah gambar berisi beberapa orang, gambar tersebut akan disalin ke folder masing-masing orang yang terdeteksi.*


## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](../LICENSE) untuk detailnya.