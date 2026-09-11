# Generator Data Siswa Sidigs Murid Dapodik (1000+ Data)

Program Python otomatis untuk menghasilkan data dummy siswa dalam jumlah besar (**1.000 hingga 10.000+ siswa**) yang **100% presisi dan kompatibel** dengan format template Excel master [`format sidigs murid-dapodik.xlsx`](format%20sidigs%20murid-dapodik.xlsx).

---

## 📋 Daftar Isi
1. [Fitur Utama](#-fitur-utama)
2. [Instalasi & Persiapan](#-instalasi--persiapan)
3. [Petunjuk Penggunaan Langkah demi Langkah](#-petunjuk-penggunaan-langkah-demi-langkah)
   - [Mode Interaktif (Tanya Jawab)](#1-mode-interaktif-tanya-jawab)
   - [Mode Perintah Langsung (CLI)](#2-mode-perintah-langsung-cli)
4. [Pilihan Jenjang Pendidikan](#-pilihan-jenjang-pendidikan)
5. [Struktur & Aturan Kolom (72 Kolom)](#-struktur--aturan-kolom-72-kolom)
6. [Panduan Import ke Sidigs / Dapodik](#-panduan-import-ke-sidigs--dapodik)
7. [Tanya Jawab & Penyelesaian Masalah (FAQ)](#-tanya-jawab--penyelesaian-masalah-faq)
8. [Struktur Proyek](#-struktur-proyek)

---

## ✨ Fitur Utama

1. **Presisi 100% dengan Format Asli Sidigs**:
   - Mempertahankan baris 1–3 catatan template (*Notes, Tanda (\*) Wajib Diisi, Kosongkan kolom jika tidak diisi*).
   - Mempertahankan *merged header* dua baris (Baris 5 & 6) pada 72 kolom data Dapodik.
   - Pengisian data dimulai tepat dari baris ke-7 sesuai file master.
2. **Kesesuaian Validasi Dropdown Excel (*Data Validation*)**:
   - Seluruh nilai dropdown (Jenis Kelamin, Jenjang Pendidikan, Penghasilan Orang Tua, Alat Transportasi, KPS, dll.) sesuai persis dengan formula validasi template.
   - Jangkauan aturan *Data Validation* diperluas otomatis hingga baris terakhir data (misal baris 1006, 2006, dst.), bukan terhenti di baris 1008.
3. **Format Data Realistis Indonesia**:
   - **Nama Asli Indonesia**: Kombinasi nama depan & belakang khas Indonesia tanpa gelar akademis.
   - **Kesesuaian Gender**: Nama pria berjenis kelamin `Laki - Laki`, nama wanita berjenis kelamin `Perempuan`.
   - **NIK Valid 16 Digit Sesuai Standar Dukcapil**: 6 digit kode wilayah Kemendagri + tanggal/bulan/tahun + nomor urut. Untuk perempuan, tanggal lahir otomatis ditambahkan 40 (`tgl + 40`).
   - **Format Tanggal**: Tersimpan sebagai objek tanggal dengan format Excel Indonesia `[$-421]d mmmm yyyy` (contoh: `12 April 2007`).
   - **Format Teks NIK & HP**: Kolom NIK, HP, dan No. KK diformat sebagai teks (`@`) sehingga angka `0` di awal tidak akan terpotong.
   - **Akun Otomatis**: Username dan password untuk murid (`budisantoso` / `budisantoso123`) serta akun wali murid (`ortubudisantoso` / `ortubudisantoso123`).
   - **Data Orang Tua**: Menghasilkan data Ayah dan Ibu dengan rentang usia realistis (~25–35 tahun lebih tua dari anak) beserta jenjang pendidikan dan penghasilannya.
4. **Auto-Detect Virtual Environment**:
   - Script otomatis mendeteksi folder `.venv` lokal sehingga dapat langsung dijalankan dengan `python generate_siswa.py` tanpa perlu aktivasi manual.
5. **Performa Tinggi**:
   - Mampu meng-generate 1.000 data dalam waktu ~2 detik.

---

## 🚀 Instalasi & Persiapan

Pastikan komputer Anda memiliki Python 3.9 atau lebih baru.

### Cara 1: Menggunakan `uv` (Sangat Cepat - Direkomendasikan)
Jika sistem Anda memiliki `uv`:
```bash
# Otomatis install dependensi dan jalankan
uv run generate_siswa.py --count 1000
```

### Cara 2: Menggunakan Python & `pip` Standar
```bash
# 1. Masuk ke folder proyek
cd /home/ard/Coding/siswa-generator

# 2. Buat virtual environment (jika belum ada)
python3 -m venv .venv

# 3. Aktifkan virtual environment
# Linux/macOS (Bash/Zsh):
source .venv/bin/activate
# Linux (Fish Shell):
source .venv/bin/activate.fish

# 4. Pasang library yang dibutuhkan
pip install -r requirements.txt
```

---

## 📖 Petunjuk Penggunaan Langkah demi Langkah

### 1. Mode Interaktif (Tanya Jawab)
Cara paling mudah tanpa perlu mengingat perintah. Cukup ketik:
```bash
python generate_siswa.py
```
Program akan menampilkan panduan tanya jawab:
1. **Jumlah Siswa**: Masukkan jumlah yang diinginkan (tekan Enter untuk default 1.000 siswa).
2. **Nama File Output**: Masukkan nama file Excel hasil (default: `hasil_siswa_{jumlah}.xlsx`). File otomatis disimpan ke dalam folder `export_excel/`.
3. **Pilihan Jenjang**: Pilih angka 1–9 sesuai tingkatan sekolah yang diinginkan.
4. **Mode Pengisian**:
   - `1` (Standar): Mengisi kolom data utama **beserta NIS dan NISN**, dengan kolom kelas tetap opsional (kosong secara default).
   - `2` (Lengkap / Full): Mengisi semua kolom tambahan Dapodik (termasuk Alamat Lengkap, No KK, Fisik BB/TB, Sekolah Asal, dsb.).
5. **Kelas / Rombel Spesifik (Opsional)**:
   - Tekan **Enter** langsung jika ingin kolom kelas **tetap kosong** (sesuai template aslinya).
   - Atau ketik nama kelas jika ingin ditentukan (misal: `X-A, X-B, X-C` atau `XII TKJ 1`).

---

### 2. Mode Perintah Langsung (CLI)

Gunakan perintah satu baris dengan berbagai parameter sesuai kebutuhan. Seluruh output file Excel otomatis tersimpan di folder **`export_excel/`**:

#### A. Generate 1.000 Siswa SMA Standar (NIS & NISN Terisi, Kelas Kosong)
```bash
python generate_siswa.py --count 1000 -o siswa_1000.xlsx
# Hasil tersimpan di: export_excel/siswa_1000.xlsx
```

#### B. Generate 1.000 Siswa Standar dengan Penyesuaian Kelas Tertentu
```bash
python generate_siswa.py --count 1000 --kelas "X-A, X-B, X-C, X-D" -o siswa_1000_kelas.xlsx
```

#### C. Generate Siswa SMK Lengkap dengan Jurusan Kejuruan
```bash
python generate_siswa.py -n 1200 --jenjang SMK --mode full -o siswa_smk_1200.xlsx
```
*Hasil otomatis berisi rombel jurusan kejuruan seperti `X-RPL-1`, `X-TKJ-1`, `X-AKL-1`, `X-DKV-1`, `X-TBSM-1`, dsb.*

#### D. Generate Siswa SMP (1.500 Siswa)
```bash
python generate_siswa.py -n 1500 --jenjang SMP -o siswa_smp_1500.xlsx
```

#### E. Generate Siswa SD / MI / TK / PAUD
```bash
# SD (Sekolah Dasar)
python generate_siswa.py -n 600 --jenjang SD -o siswa_sd_600.xlsx

# TK / PAUD
python generate_siswa.py -n 250 --jenjang TK -o siswa_tk_250.xlsx
```

#### F. Generate Siswa SLB (Sekolah Luar Biasa)
```bash
python generate_siswa.py -n 100 --jenjang SLB --mode full -o siswa_slb_100.xlsx
```
*Kolom Kebutuhan Khusus otomatis terisi: Tunarungu, Tunanetra, Tunadaksa, Tunagrahita, atau Autis.*

---

## 🏫 Pilihan Jenjang Pendidikan

Program mendukung 9 pilihan jenjang pendidikan nasional:

| No | Kode / Alias | Nama Lengkap | Usia Siswa | Contoh Rombel Otomatis | Sekolah Asal |
|:---:|:---:|:---|:---:|:---|:---|
| **1** | `SMA` | Sekolah Menengah Atas *(Default)* | ~15–18 th | `X-1`, `X-2`, `XI-MIPA-1`, `XII-IPS-1` | SMP Negeri |
| **2** | `SMK` | Sekolah Menengah Kejuruan | ~15–18 th | `X-RPL-1`, `X-TKJ-1`, `X-AKL-1`, `X-DKV-1` | SMP Negeri |
| **3** | `SMP` | Sekolah Menengah Pertama | ~12–15 th | `VII-A`, `VII-B`, `VIII-A`, `IX-A` | SD Negeri |
| **4** | `SD` | Sekolah Dasar | ~6–12 th | `I-A`, `II-A`, `III-A`, `IV-A`, dst. | TK Pertiwi |
| **5** | `TK` / `PAUD` | Pendidikan Anak Usia Dini | ~4–6 th | `Kelompok A-1`, `Kelompok B-1` | Posyandu / PAUD |
| **6** | `MA` | Madrasah Aliyah | ~15–18 th | `X-1`, `XI-MIPA`, `XI-Keagamaan` | MTs Negeri |
| **7** | `MTS` | Madrasah Tsanawiyah | ~12–15 th | `7-A`, `7-B`, `8-A`, `9-A` | MI / SD Negeri |
| **8** | `MI` | Madrasah Ibtidaiyah | ~6–12 th | `1-A`, `2-A`, `3-A`, dst. | RA (Raudhatul Athfal) |
| **9** | `SLB` | Sekolah Luar Biasa | ~7–17 th | `Kelas A`, `Kelas B`, `Kelas C`, `Kelas Autis` | SDLB / Terapi |

---

## 📊 Struktur & Aturan Kolom (72 Kolom)

Format Excel Sidigs memiliki **72 kolom**. Berikut pedoman pengisiannya:

### Kolom Wajib Bertanda `(*)`
Berdasarkan aturan template pada baris ke-2: **Tanda (\*) Wajib Diisi**.
- **Kolom 2 (B)**: `Nama (*)`
- **Kolom 7 (G)**: `Jenis Kelamin (*)`
- **Kolom 9 (I)**: `Tempat Lahir (*)`
- **Kolom 10 (J)**: `Tanggal Lahir (*)`
- **Kolom 31 (AE)**: `Tanggal Lahir (*) Ayah`
- **Kolom 37 (AK)**: `Tanggal Lahir (*) Ibu`

### Kolom Identitas Siswa (NIS & NISN - Otomatis Terisi)
- **Kolom 6 (F) - `NIS`**: Nomor Induk Siswa 5 digit berurutan (contoh: `24001`, `24002`, dst.). Diformat sebagai Text (`@`).
- **Kolom 8 (H) - `NISN`**: Nomor Induk Siswa Nasional 10 digit standar nasional (diawali `0` + 2 digit tahun lahir + 7 digit nomor unik, misal: `0091049914`). Diformat sebagai Text (`@`) sehingga angka nol di awal tidak hilang.

### Kolom Kelas / Rombel (`Rombel Saat Ini` - Kolom 48 / AV - Tetap Opsional)
- **Status**: **OPSIONAL** (tidak memiliki tanda `*`).
- **Default di Mode Standar**: Dibiarkan **kosong (`None`)** persis seperti data contoh bawaan file Sidigs (Budi Santoso & Anisa Rahmawati).
- **Fleksibel Disesuaikan**: Jika Anda ingin mengisi kelas, Anda bisa:
  - Mengisi saat ditanya di Mode Interaktif (Langkah 5).
  - Atau menggunakan opsi `--kelas` / `-r` di CLI (misal: `--kelas "X-A, X-B, X-C"` untuk pembagian kelas otomatis).

### Kolom Kredensial Akun Login
- **Kolom 4 & 5 (D & E)**: Username & Password Login Murid (contoh: `budisantoso` / `budisantoso123`).
- **Kolom 28 & 29 (AB & AC)**: Username & Password Login Wali Murid (contoh: `ortubudisantoso` / `ortubudisantoso123`).

---

## 📥 Panduan Import ke Sidigs / Dapodik

1. **Jalankan program generator**:
   ```bash
   python generate_siswa.py --count 1000 -o siswa_siap_import.xlsx
   ```
2. **Cek File Output**:
   - Buka file di folder **`export_excel/siswa_siap_import.xlsx`** menggunakan Microsoft Excel, LibreOffice Calc, atau WPS Office.
   - Pastikan data dimulai dari baris ke-7 dan baris 1–6 tetap utuh.
3. **Upload ke Sistem Sidigs**:
   - Masuk ke menu **Import Siswa / Murid** di portal Sidigs.
   - Pilih template Excel dari folder `export_excel/` hasil generator tadi.
   - Klik **Upload / Proses Import**.
   - Karena format dropdown dan tipe datanya sudah 100% presisi, sistem tidak akan menampilkan error validasi tipe data.

---

## ❓ Tanya Jawab & Penyelesaian Masalah (FAQ)

### Q1: Muncul `Error: Package 'openpyxl' belum terpasang`?
**Solusi:** Script versi terbaru sudah memiliki fitur *auto-detect*. Pastikan folder `.venv` ada di direktori proyek, atau jalankan melalui `uv`:
```bash
uv run generate_siswa.py --count 1000
```
Atau aktifkan venv terlebih dahulu:
```bash
source .venv/bin/activate && python generate_siswa.py --count 1000
```

### Q2: Apakah NIK dan No HP aman dari kehilangan angka `0` di depan?
**Solusi:** Ya, sangat aman. Seluruh kolom NIK (Kolom K), HP (Kolom W), dan No. KK (Kolom BN) otomatis diberi tipe format sel Text (`@`). Angka nol di depan (misal `0812...` atau `007...`) tidak akan terpotong menjadi angka desimal.

### Q3: Apakah bisa generate lebih dari 1.000 data (misal 5.000 data)?
**Solusi:** Tentu bisa! Cukup ubah nilainya:
```bash
python generate_siswa.py --count 5000 -o siswa_5000.xlsx
```
Program otomatis memperluas aturan Data Validation Excel hingga baris ke-5006 dan menyimpan hasilnya ke `export_excel/siswa_5000.xlsx`.

### Q4: Apakah saya bisa mereproduksi data yang sama persis?
**Solusi:** Gunakan opsi `--seed`:
```bash
python generate_siswa.py --count 1000 --seed 42 -o siswa_reproducible.xlsx
```

---

## 📁 Struktur Proyek

```
siswa-generator/
├── generate_siswa.py               # Entrypoint utama script generator
├── generator/                      # Package modular (mudah di-maintain & di-fix)
│   ├── __init__.py                 # Export modul utama
│   ├── constants.py                # Konstanta (Agama, Pekerjaan, Transportasi, dsb.)
│   ├── names.py                    # Dataset nama depan laki/perempuan & nama belakang
│   ├── locations.py                # Data kota, wilayah, kode pos, dan alamat
│   ├── jenjang.py                  # Konfigurasi jenjang sekolah (SMA, SMK, SMP, SD, TK, SLB)
│   ├── student.py                  # Logika pembuatan data siswa, NIK, username, orang tua
│   ├── excel.py                    # Manipulasi Excel (openpyxl, styling, Data Validation)
│   └── cli.py                      # Antarmuka CLI & mode interaktif tanya-jawab
├── export_excel/                   # Folder penampung semua file Excel hasil generate (di-ignore git)
│   └── siswa_sidigs_1000.xlsx      # File contoh 1.000 siswa siap pakai
├── format sidigs murid-dapodik.xlsx # File template master Sidigs Dapodik (di-ignore git)
├── pyproject.toml                  # Konfigurasi packaging Python / uv
├── requirements.txt                # Daftar library dependensi
├── .gitignore                      # Aturan pengabaian file Excel, venv, cache
└── README.md                       # Petunjuk dokumentasi lengkap ini
```
