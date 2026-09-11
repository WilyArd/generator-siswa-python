#!/usr/bin/env python3
"""
Siswa Generator untuk Format Sidigs Murid Dapodik
=================================================
Script otomatis untuk membuat data dummy siswa hingga 1000+ data
yang 100% kompatibel dan presisi dengan template:
'format sidigs murid-dapodik.xlsx'

Struktur kode telah dimodularisasi ke dalam package 'generator/':
- generator/constants.py : Pilihan agama, transportasi, pekerjaan, penghasilan
- generator/names.py     : Kumpulan nama depan & belakang Indonesia
- generator/locations.py : Data kota, kode wilayah Dukcapil, alamat
- generator/jenjang.py   : Konfigurasi jenjang sekolah (SMA, SMK, SMP, SD, TK, SLB)
- generator/student.py   : Logika pembentukan akun, NIK, dan baris data siswa
- generator/excel.py     : Penanganan file Excel, styling, dan Data Validation
- generator/cli.py       : Antarmuka perintah baris (CLI) & mode interaktif
"""

import os
import sys

# 1. Pastikan direktori project berada dalam sys.path
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# 2. Pemeriksaan dependensi & auto-detect virtual environment lokal
try:
    import openpyxl
except ImportError:
    venv_python = os.path.join(PROJECT_DIR, ".venv", "bin", "python")
    if os.path.exists(venv_python) and os.path.realpath(sys.executable) != os.path.realpath(venv_python):
        # Jalankan ulang secara transparan menggunakan Python dari .venv
        os.execv(venv_python, [venv_python] + sys.argv)

    print("=" * 60)
    print("Error: Package 'openpyxl' belum terpasang di environment Python ini.")
    print("=" * 60)
    print("Solusi cepat, jalankan salah satu perintah berikut:")
    print("  1. Menggunakan uv (direkomendasikan):")
    print(f"     uv run python {' '.join(sys.argv)}")
    print("  2. Aktifkan virtual environment yang sudah ada:")
    print("     source .venv/bin/activate")
    print(f"     python {' '.join(sys.argv)}")
    print("  3. Atau jalankan langsung via Python virtual environment:")
    print(f"     .venv/bin/python {' '.join(sys.argv)}")
    print("=" * 60)
    sys.exit(1)

# 3. Import fungsi utama dari package generator
from generator.excel import generate_siswa_excel
from generator.student import generate_single_student, generate_nik, clean_username
from generator.jenjang import JENJANG_CONFIG, normalize_jenjang
from generator.cli import main, interactive_prompt


if __name__ == "__main__":
    main()
