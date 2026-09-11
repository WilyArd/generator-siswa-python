#!/usr/bin/env python3
"""
Siswa Generator untuk Format Sidigs Murid Dapodik
=================================================
Script otomatis untuk membuat data dummy siswa hingga 1000+ data
yang 100% kompatibel dan presisi dengan template:
'format sidigs murid-dapodik.xlsx'
"""

import os
import sys
import re
import random
import datetime
import argparse
from copy import copy

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    # Cek apakah terdapat .venv lokal yang sudah memiliki openpyxl
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_python = os.path.join(script_dir, ".venv", "bin", "python")
    if os.path.exists(venv_python) and os.path.realpath(sys.executable) != os.path.realpath(venv_python):
        # Jalankan ulang secara otomatis menggunakan Python dari .venv
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

# Cek Faker jika tersedia, jika tidak script tetap berjalan dengan built-in dataset
try:
    from faker import Faker
    fake = Faker('id_ID')
    HAS_FAKER = True
except ImportError:
    fake = None
    HAS_FAKER = False

# ==============================================================================
# DATASET REALISTIS INDONESIA (BUILT-IN)
# ==============================================================================
NAMA_DEPAN_LAKI = [
    "Muhammad", "Ahmad", "Dimas", "Rizky", "Kevin", "Arya", "Bayu", "Fadhil",
    "Bagus", "Ilham", "Farhan", "Aditya", "Rayhan", "Daffa", "Rio", "Aldo",
    "Gilang", "Fajar", "Rian", "Wahyu", "Yusuf", "Denis", "Rama", "Danu",
    "Rendy", "Reza", "Satria", "Iqbal", "Alif", "Haikal", "Aris", "Tegar",
    "Bintang", "Galang", "Rifki", "Angga", "Doni", "Vicky", "Hendra", "Yoga",
    "Pratama", "Surya", "Brian", "Naufal", "Zaki", "Dzaky", "Andre", "Fauzan",
    "Faisal", "Eko", "Bambang", "Agus", "Budi", "Tri", "Joko", "Hadi",
    "Dwi", "Arif", "Hendra", "Agung", "Wahid", "Zainal", "Anwar", "Ridwan",
    "Lukman", "Rahmat", "Syahrul", "Taufik", "Zulham", "Arga", "Rendra", "Farid",
    "Ghafi", "Kurnia", "Mahendra", "Pandu", "Raffi", "Sultan", "Tirta", "Vino",
    "Wisnu", "Yandi", "Zidan", "Akbar", "Bilal", "Candra", "Danang", "Fikri",
    "Giri", "Haris", "Irfan", "Julian", "Kharisma", "Latif", "Maulana", "Noval",
    "Oki", "Panji", "Rasyid", "Sandi", "Tomi", "Wildan", "Yayan", "Zulfa"
]

NAMA_DEPAN_PEREMPUAN = [
    "Siti", "Annisa", "Nabila", "Putri", "Zahra", "Aulia", "Nurul", "Tiara",
    "Dewi", "Indah", "Maya", "Rina", "Salma", "Fitri", "Amanda", "Bella",
    "Cindy", "Dinda", "Eka", "Farah", "Gita", "Hana", "Intan", "Jessica",
    "Karina", "Lestari", "Melani", "Nadia", "Olivia", "Pratiwi", "Qonita", "Rahma",
    "Safira", "Tasya", "Ulfa", "Vina", "Wulan", "Yasmin", "Zaskia", "Cantika",
    "Clarissa", "Syifa", "Nayla", "Alya", "Ayu", "Chandra", "Desi", "Erna",
    "Fani", "Gisella", "Hesti", "Ika", "Juwita", "Kania", "Lia", "Mega",
    "Novita", "Oktavia", "Poppy", "Rania", "Siska", "Tari", "Utari", "Vivi",
    "Winda", "Yulia", "Zulfa", "Adelia", "Balqis", "Chelsea", "Dhea", "Elvira",
    "Fadila", "Ghina", "Halimah", "Isyana", "Kamila", "Laras", "Mutia", "Nadira"
]

NAMA_BELAKANG = [
    "Pratama", "Saputra", "Hidayat", "Santoso", "Wibowo", "Setiawan", "Wijaya", "Kusuma",
    "Utomo", "Nugroho", "Lestari", "Anggraini", "Ramadhan", "Firmansyah", "Prasetyo", "Kurniawan",
    "Mahendra", "Subagyo", "Suherman", "Suryanto", "Suhendra", "Priyanto", "Budiman", "Gunawan",
    "Wardhana", "Sulaeman", "Iskandar", "Supriyadi", "Darmawan", "Siregar", "Nasution", "Hasibuan",
    "Harahap", "Batubara", "Pasaribu", "Simanjuntak", "Hutapea", "Panjaitan", "Manurung", "Sinaga",
    "Siahaan", "Ginting", "Tarigan", "Sembiring", "Lubis", "Daulay", "Tanjung", "Chaniago",
    "Piliang", "Koto", "Sikumbang", "Marpaung", "Sitompul", "Purba", "Saragih", "Situmorang",
    "Hutabarat", "Panggabean", "Hakim", "Fauzi", "Munandar", "Mustofa", "Baskoro", "Wahyudi",
    "Yulianto", "Sucipto", "Purnama", "Kurnia", "Alamsyah", "Sudirman", "Hartono", "Permana"
]

KOTA_WILAYAH = [
    # (Nama Kota, Kode Wilayah 6 digit Kemendagri, Kelurahan List, Kecamatan List, Kode Pos List)
    ("Trenggalek", "350301", ["Ngetal", "Kelutan", "Sumbergedong", "Ngantru", "Surodakan", "Durenan", "Karangan"], ["Pogalan", "Trenggalek", "Durenan", "Karangan", "Gandusari"], [66371, 66311, 66312, 66381]),
    ("Tulungagung", "350401", ["Bago", "Kepatihan", "Kampungdalem", "Tertek", "Kenayan", "Sembung", "Kutoanyar"], ["Tulungagung", "Kedungwaru", "Boyolangu", "Kauman", "Ngunut"], [66212, 66213, 66217, 66219]),
    ("Batu", "357901", ["Sisir", "Temas", "Songgokerto", "Oro-oro Ombo", "Sidomulyo", "Bumiaji", "Pesanggrahan"], ["Batu", "Bumiaji", "Junrejo"], [65311, 65314, 65315, 65331]),
    ("Malang", "357301", ["Klojen", "Lowokwaru", "Sukun", "Blimbing", "Kedungkandang", "Dinoyo", "Tulusrejo"], ["Klojen", "Lowokwaru", "Sukun", "Blimbing", "Kedungkandang"], [65111, 65141, 65144, 65126]),
    ("Surabaya", "357801", ["Gubeng", "Wonokromo", "Rungkut", "Tegalsari", "Tambaksari", "Sawahan", "Sukolilo"], ["Gubeng", "Wonokromo", "Rungkut", "Tegalsari", "Tambaksari"], [60281, 60241, 60293, 60262]),
    ("Kediri", "357101", ["Mojoroto", "Pesantren", "Kota", "Banjaran", "Ngronggo", "Semampir"], ["Mojoroto", "Kota", "Pesantren"], [64111, 64121, 64131]),
    ("Blitar", "357201", ["Kepanjenkidul", "Sukorejo", "Sananwetan", "Bendo", "Kauman"], ["Kepanjenkidul", "Sukorejo", "Sananwetan"], [66111, 66121, 66131]),
    ("Sidoarjo", "351501", ["Sidokumpul", "Pucang", "Lemahputro", "Magersari", "Celep", "Waru"], ["Sidoarjo", "Waru", "Candi", "Buduran"], [61212, 61213, 61256]),
    ("Bandung", "327301", ["Coblong", "Cicendo", "Regol", "Batununggal", "Lengkong", "Cibeunying"], ["Coblong", "Cicendo", "Regol", "Lengkong"], [40132, 40171, 40251]),
    ("Jakarta Selatan", "317401", ["Kebayoran Baru", "Cilandak", "Pasar Minggu", "Tebet", "Mampang Prapatan"], ["Kebayoran Baru", "Cilandak", "Pasar Minggu", "Tebet"], [12110, 12430, 12520, 12810]),
    ("Semarang", "337401", ["Semarang Barat", "Semarang Timur", "Banyumanik", "Pedurungan", "Candisari"], ["Semarang Barat", "Semarang Timur", "Banyumanik"], [50141, 50125, 50268]),
    ("Yogyakarta", "347101", ["Danurejan", "Gondomanan", "Kraton", "Mantrijeron", "Umbulharjo"], ["Danurejan", "Gondomanan", "Umbulharjo"], [55211, 55122, 55161])
]

AGAMA_LIST = ["Islam", "Islam", "Islam", "Islam", "Islam", "Islam", "Islam", "Islam", "Kristen", "Katolik", "Hindu", "Buddha"]

JENIS_TINGGAL_LIST = ["Bersama orang tua", "ORANGTUA", "Bersama orang tua", "ORANGTUA", "Wali", "Kost"]

TRANSPORTASI_LIST = ["Jalan Kaki", "Sepeda", "Sepeda Motor", "Sepeda Motor", "Ojek", "Mobil Pribadi", "Lainnnya"]

PENDIDIKAN_LIST = [
    "SD Sederajat", "SMP Sederajat", "SMA Sederajat", "SMA Sederajat",
    "S1 / D4", "S1 / D4", "D3", "D1", "S2"
]

PEKERJAAN_AYAH_LIST = [
    "Wiraswasta", "Karyawan Swasta", "PNS / Guru", "Buruh",
    "Pedagang", "Petani", "Sopir", "TNI / Polri", "Tukang Kayu / Bangunan"
]

PEKERJAAN_IBU_LIST = [
    "Ibu Rumah Tangga", "Ibu Rumah Tangga", "Ibu Rumah Tangga",
    "Karyawan Swasta", "Wiraswasta", "Pedagang", "PNS / Guru", "Buruh"
]

PENGHASILAN_LIST = [
    "Tidak Berpenghasilan",
    "Kurang Dari Rp.500.000",
    "Rp.500.000 - Rp.999.999",
    "Rp.1.000.000 - Rp.1.999.999",
    "Rp.2.000.000 - Rp.3.499.999",
    "Rp.3.500.000 - Rp.4.999.999",
    "Rp.5.000.000 - Rp.9.999.999",
    "Rp.10.000.000 - Rp.20.000.000"
]

PREFIX_HP = ["0812", "0813", "0821", "0822", "0852", "0853", "0857", "0858", "0877", "0878", "0895", "0896"]

# ==============================================================================
# KONFIGURASI JENJANG PENDIDIKAN
# ==============================================================================
JENJANG_CONFIG = {
    "SMA": {
        "nama": "SMA (Sekolah Menengah Atas)",
        "min_age": 15, "max_age": 18,
        "classes": ["X-1", "X-2", "X-3", "X-4", "XI-MIPA-1", "XI-IPS-1", "XII-MIPA-1", "XII-IPS-1"],
        "sekolah_asal": "SMP Negeri",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "SMK": {
        "nama": "SMK (Sekolah Menengah Kejuruan)",
        "min_age": 15, "max_age": 18,
        "classes": ["X-RPL-1", "X-RPL-2", "X-TKJ-1", "X-TKJ-2", "X-AKL-1", "X-DKV-1", "X-TBSM-1", "X-MP-1"],
        "sekolah_asal": "SMP Negeri",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "SMP": {
        "nama": "SMP (Sekolah Menengah Pertama)",
        "min_age": 12, "max_age": 15,
        "classes": ["VII-A", "VII-B", "VII-C", "VII-D", "VIII-A", "VIII-B", "IX-A", "IX-B"],
        "sekolah_asal": "SD Negeri",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "MTS": {
        "nama": "MTs (Madrasah Tsanawiyah)",
        "min_age": 12, "max_age": 15,
        "classes": ["7-A", "7-B", "7-C", "7-D", "8-A", "8-B", "9-A", "9-B"],
        "sekolah_asal": "MI / SD Negeri",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "MA": {
        "nama": "MA (Madrasah Aliyah)",
        "min_age": 15, "max_age": 18,
        "classes": ["X-1", "X-2", "XI-MIPA", "XI-IPS", "XI-Keagamaan", "XII-MIPA", "XII-IPS"],
        "sekolah_asal": "MTs Negeri",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "SD": {
        "nama": "SD (Sekolah Dasar)",
        "min_age": 6, "max_age": 12,
        "classes": ["I-A", "I-B", "II-A", "II-B", "III-A", "IV-A", "V-A", "VI-A"],
        "sekolah_asal": "TK Pertiwi",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "MI": {
        "nama": "MI (Madrasah Ibtidaiyah)",
        "min_age": 6, "max_age": 12,
        "classes": ["1-A", "1-B", "2-A", "2-B", "3-A", "4-A", "5-A", "6-A"],
        "sekolah_asal": "RA (Raudhatul Athfal)",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "TK": {
        "nama": "TK / PAUD (Pendidikan Anak Usia Dini)",
        "min_age": 4, "max_age": 6,
        "classes": ["Kelompok A-1", "Kelompok A-2", "Kelompok B-1", "Kelompok B-2"],
        "sekolah_asal": "PAUD / Posyandu",
        "kebutuhan_khusus": "Tidak Ada"
    },
    "SLB": {
        "nama": "SLB (Sekolah Luar Biasa)",
        "min_age": 7, "max_age": 17,
        "classes": ["Kelas A", "Kelas B", "Kelas C", "Kelas D", "Kelas Autis"],
        "sekolah_asal": "SDLB / Terapi Mandiri",
        "kebutuhan_khusus": ["Tunarungu", "Tunanetra", "Tunagrahita", "Tunadaksa", "Autis"]
    }
}


def normalize_jenjang(level_str: str) -> str:
    """Normalisasi input jenjang ke kode standar."""
    if not level_str:
        return "SMA"
    s = level_str.strip().upper()
    alias_map = {
        "PAUD": "TK",
        "TAMAN KANAK-KANAK": "TK",
        "TAMAN KANAK KANAK": "TK",
        "MADRASAH ALIYAH": "MA",
        "MADRASAH TSANAWIYAH": "MTS",
        "MADRASAH IBTIDAIYAH": "MI",
        "KEJURUAN": "SMK",
    }
    key = alias_map.get(s, s)
    return key if key in JENJANG_CONFIG else "SMA"


def clean_username(text: str) -> str:
    """Mengubah teks nama menjadi username tanpa spasi dan karakter khusus."""
    clean = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return clean[:20] if len(clean) > 20 else clean


def generate_nik(wilayah_code: str, tgl: int, bln: int, thn: int, is_female: bool, urut: int) -> str:
    """
    Menghasilkan 16 digit NIK Indonesia yang realistis sesuai standar Dukcapil:
    - 6 digit kode wilayah (Provinsi + Kab/Kota + Kec)
    - 2 digit tanggal (wanita + 40)
    - 2 digit bulan
    - 2 digit tahun
    - 4 digit nomor urut unik
    """
    dd = tgl + 40 if is_female else tgl
    yy = thn % 100
    serial = (urut % 9999) + 1
    return f"{wilayah_code}{dd:02d}{bln:02d}{yy:02d}{serial:04d}"


def generate_single_student(idx: int, level: str, mode: str, used_usernames: set, rombel_input: str = None):
    """
    Menghasilkan data lengkap 1 siswa yang siap dimasukkan ke baris Excel Sidigs Dapodik.
    """
    # 1. Gender & Nama
    is_male = (idx % 2 == 1) if random.random() < 0.9 else (random.choice([True, False]))
    jenis_kelamin = "Laki - Laki" if is_male else "Perempuan"

    if is_male:
        first_name = random.choice(NAMA_DEPAN_LAKI)
    else:
        first_name = random.choice(NAMA_DEPAN_PEREMPUAN)

    mid_or_last = random.choice(NAMA_BELAKANG)
    if random.random() < 0.4:
        third_name = random.choice(NAMA_BELAKANG)
        while third_name == mid_or_last:
            third_name = random.choice(NAMA_BELAKANG)
        full_name = f"{first_name} {mid_or_last} {third_name}"
    else:
        full_name = f"{first_name} {mid_or_last}"

    nama_panggilan = first_name

    # 2. Username & Password Murid
    base_user = clean_username(f"{first_name}{mid_or_last}")
    username = base_user
    counter = 1
    while username in used_usernames or len(username) < 4:
        username = f"{base_user}{counter}"
        counter += 1
    used_usernames.add(username)
    password = f"{username}123"

    # 3. Akun Wali Murid
    username_wali = f"ortu{username}"
    password_wali = f"ortu{username}123"

    # 4. Tanggal Lahir Siswa
    cfg = JENJANG_CONFIG.get(normalize_jenjang(level), JENJANG_CONFIG["SMA"])
    curr_year = datetime.datetime.now().year
    birth_year = random.randint(curr_year - cfg["max_age"], curr_year - cfg["min_age"])
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    tgl_lahir_siswa = datetime.datetime(birth_year, birth_month, birth_day, 0, 0)

    # 5. Kota, Wilayah & NIK
    kota_info = random.choice(KOTA_WILAYAH)
    tempat_lahir = kota_info[0]
    wilayah_code = kota_info[1]
    kelurahan = random.choice(kota_info[2])
    kecamatan = random.choice(kota_info[3])
    kode_pos = random.choice(kota_info[4])
    dusun = "-" if random.random() < 0.6 else f"Dusun {random.choice(['Krajan', 'Kebon', 'Duwet', 'Kedung', 'Sumber', 'Tengah'])}"

    nik_siswa = generate_nik(wilayah_code, birth_day, birth_month, birth_year, not is_male, idx)

    # 6. Alamat & Kontak
    rt = random.randint(1, 20)
    rw = random.randint(1, 12)
    alamat = f"Jl. {random.choice(['Melati', 'Mawar', 'Diponegoro', 'Sudirman', 'Gajah Mada', 'Pahlawan', 'Merdeka'])} No. {random.randint(1, 150)}"
    hp_prefix = random.choice(PREFIX_HP)
    hp_suffix = f"{random.randint(10000000, 99999999):08d}"
    hp = f"{hp_prefix}{hp_suffix}"

    agama = random.choice(AGAMA_LIST)
    jenis_tinggal = random.choice(JENIS_TINGGAL_LIST)
    alat_transportasi = random.choice(TRANSPORTASI_LIST)

    # 7. Data Orang Tua (Ayah & Ibu)
    # Ayah
    ayah_first = random.choice(NAMA_DEPAN_LAKI)
    ayah_last = random.choice(NAMA_BELAKANG)
    nama_ayah = f"{ayah_first} {ayah_last}".upper() if random.random() < 0.5 else f"{ayah_first} {ayah_last}"
    ayah_birth_year = birth_year - random.randint(25, 36)
    ayah_tgl_lahir = datetime.datetime(ayah_birth_year, random.randint(1, 12), random.randint(1, 28), 0, 0)
    ayah_pendidikan = random.choice(PENDIDIKAN_LIST)
    ayah_pekerjaan = random.choice(PEKERJAAN_AYAH_LIST)
    ayah_penghasilan = random.choice(PENGHASILAN_LIST)
    ayah_nik = generate_nik(wilayah_code, ayah_tgl_lahir.day, ayah_tgl_lahir.month, ayah_birth_year, False, idx + 1000)

    # Ibu
    ibu_first = random.choice(NAMA_DEPAN_PEREMPUAN)
    ibu_last = random.choice(NAMA_BELAKANG)
    nama_ibu = f"{ibu_first} {ibu_last}".upper() if random.random() < 0.5 else f"{ibu_first} {ibu_last}"
    ibu_birth_year = birth_year - random.randint(22, 33)
    ibu_tgl_lahir = datetime.datetime(ibu_birth_year, random.randint(1, 12), random.randint(1, 28), 0, 0)
    ibu_pendidikan = random.choice(PENDIDIKAN_LIST)
    ibu_pekerjaan = random.choice(PEKERJAAN_IBU_LIST)
    ibu_penghasilan = "Tidak Berpenghasilan" if "Rumah Tangga" in ibu_pekerjaan else random.choice(PENGHASILAN_LIST)
    ibu_nik = generate_nik(wilayah_code, ibu_tgl_lahir.day, ibu_tgl_lahir.month, ibu_birth_year, True, idx + 2000)

    # 8. Nomor Identitas Siswa (NIS & NISN - terisi baik di mode standar maupun full)
    # NIS: 5 digit nomor induk siswa berurutan (misal: 24001, 24002, ...)
    nis = f"{24000 + idx}"
    # NISN: 10 digit standar nasional (0 + 2 digit tahun lahir + 7 digit nomor acak unik)
    nisn = f"0{birth_year % 100:02d}{random.randint(1000000, 9999999):07d}"

    # 9. Rombel / Kelas (Opsional)
    if rombel_input:
        classes = [c.strip() for c in rombel_input.split(",") if c.strip()]
        rombel = classes[(idx - 1) % len(classes)] if classes else None
    elif mode == "full":
        rombel = random.choice(cfg["classes"])
    else:
        rombel = None  # Tetap opsional / kosong secara default pada mode standar

    # 10. Data Tambahan Dapodik (jika mode full)
    no_kk = f"{wilayah_code}{random.randint(1000000000, 9999999999)}" if mode == "full" else None
    anak_ke = random.randint(1, 3) if mode == "full" else None
    jml_saudara = random.randint(0, 3) if mode == "full" else None
    bb = random.randint(45, 68) if mode == "full" else None
    tb = random.randint(150, 175) if mode == "full" else None
    jarak_km = random.randint(1, 12) if mode == "full" else None
    sekolah_asal = f"{cfg['sekolah_asal']} {random.randint(1, 5)} {tempat_lahir}" if mode == "full" else None
    if isinstance(cfg["kebutuhan_khusus"], list):
        kebutuhan_khusus = random.choice(cfg["kebutuhan_khusus"])
    else:
        kebutuhan_khusus = cfg["kebutuhan_khusus"] if mode == "full" else None

    # Array nilai 72 kolom (index 0..71 sesuai Col 1..72)
    # Sesuai template: standard mode persis mengikuti contoh baris 7 & 8
    row_values = [
        idx,                          # Col 1 (A): No
        full_name,                    # Col 2 (B): Nama (*)
        nama_panggilan,               # Col 3 (C): Nama Panggilan
        username,                     # Col 4 (D): Username Login Murid
        password,                     # Col 5 (E): Password Login Murid
        nis,                          # Col 6 (F): NIS
        jenis_kelamin,                # Col 7 (G): Jenis Kelamin (*)
        nisn,                         # Col 8 (H): NISN
        tempat_lahir,                 # Col 9 (I): Tempat Lahir (*)
        tgl_lahir_siswa,              # Col 10 (J): Tanggal Lahir (*)
        nik_siswa,                    # Col 11 (K): NIK
        agama,                        # Col 12 (L): Agama
        alamat if mode == "full" else None,  # Col 13 (M): Alamat
        rt,                           # Col 14 (N): RT
        rw,                           # Col 15 (O): RW
        dusun,                        # Col 16 (P): Dusun
        kelurahan,                    # Col 17 (Q): Kelurahan
        kecamatan,                    # Col 18 (R): Kecamatan
        kode_pos,                     # Col 19 (S): Kode Pos
        jenis_tinggal,                # Col 20 (T): Jenis Tinggal
        alat_transportasi,            # Col 21 (U): Alat Transportasi
        "-",                          # Col 22 (V): Telepon
        hp,                           # Col 23 (W): HP
        "-",                          # Col 24 (X): Email
        "-",                          # Col 25 (Y): SKHUN
        "Tidak",                      # Col 26 (Z): Penerima KPS
        "-",                          # Col 27 (AA): No. KPS
        username_wali,                # Col 28 (AB): Username Login Walimurid
        password_wali,                # Col 29 (AC): Password Login Walimurid
        nama_ayah,                    # Col 30 (AD): Data Ayah - Nama
        ayah_tgl_lahir,               # Col 31 (AE): Data Ayah - Tanggal Lahir (*)
        ayah_pendidikan,              # Col 32 (AF): Data Ayah - Jenjang Pendidikan
        ayah_pekerjaan if mode == "full" else None,  # Col 33 (AG): Pekerjaan
        ayah_penghasilan,             # Col 34 (AH): Penghasilan
        ayah_nik if mode == "full" else None,        # Col 35 (AI): NIK Ayah
        nama_ibu,                     # Col 36 (AJ): Data Ibu - Nama
        ibu_tgl_lahir,                # Col 37 (AK): Data Ibu - Tanggal Lahir (*)
        ibu_pendidikan,               # Col 38 (AL): Data Ibu - Jenjang Pendidikan
        ibu_pekerjaan if mode == "full" else None,   # Col 39 (AM): Pekerjaan
        ibu_penghasilan,              # Col 40 (AN): Penghasilan
        ibu_nik if mode == "full" else None,         # Col 41 (AO): NIK Ibu
        None,                         # Col 42 (AP): Data Wali - Nama
        None,                         # Col 43 (AQ): Tanggal Lahir Wali
        None,                         # Col 44 (AR): Jenjang Pendidikan Wali
        None,                         # Col 45 (AS): Pekerjaan Wali
        None,                         # Col 46 (AT): Penghasilan Wali
        None,                         # Col 47 (AU): NIK Wali
        rombel,                       # Col 48 (AV): Rombel Saat Ini
        None,                         # Col 49 (AW): Nomor Peserta UN
        None,                         # Col 50 (AX): Nomor Seri Ijazah
        "Tidak" if mode == "full" else None, # Col 51 (AY): Penerima KIP
        None,                         # Col 52 (AZ): Nomor KIP
        None,                         # Col 53 (BA): Nama Di KIP
        None,                         # Col 54 (BB): Nomor KKS
        None,                         # Col 55 (BC): No Registrasi Akta Lahir
        None,                         # Col 56 (BD): Bank
        None,                         # Col 57 (BE): Nomor Rekening Bank
        None,                         # Col 58 (BF): Rekening Atas Nama
        None,                         # Col 59 (BG): Layak PIP
        None,                         # Col 60 (BH): Alasan Layak PIP
        kebutuhan_khusus,             # Col 61 (BI): Kebutuhan Khusus
        sekolah_asal,                 # Col 62 (BJ): Sekolah Asal
        anak_ke,                      # Col 63 (BK): Anak Ke Berapa
        None,                         # Col 64 (BL): Lintang
        None,                         # Col 65 (BM): Bujur
        no_kk,                        # Col 66 (BN): No. KK
        bb,                           # Col 67 (BO): Berat Badan
        tb,                           # Col 68 (BP): Tinggi Badan
        None,                         # Col 69 (BQ): Lingkar Kepala
        jml_saudara,                  # Col 70 (BR): Jml. Saudara Kandung
        jarak_km,                     # Col 71 (BS): Jarak Rumah ke Sekolah
        None                          # Col 72 (BT): Nomor Virtual Account
    ]

    return row_values


def generate_siswa_excel(template_path: str, output_path: str, count: int = 1000, level: str = "SMA", mode: str = "standard", rombel: str = None, seed: int = None):
    """
    Fungsi utama untuk membaca template, meng-generate N data siswa, dan menyimpan hasilnya.
    """
    if seed is not None:
        random.seed(seed)

    print(f"\n[+] Memuat template: {template_path}")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"File template '{template_path}' tidak ditemukan!")

    wb = openpyxl.load_workbook(template_path)
    sheet_name = wb.sheetnames[0]
    ws = wb[sheet_name]

    cfg = JENJANG_CONFIG.get(normalize_jenjang(level), JENJANG_CONFIG["SMA"])
    print(f"[+] Sheet aktif: '{sheet_name}'")
    rombel_info = f", Kelas/Rombel: {rombel}" if rombel else (", Kelas: Acak Full" if mode == "full" else ", Kelas: Kosong (Opsional)")
    print(f"[+] Menghasilkan {count:,} data siswa (Jenjang: {cfg['nama']}, Mode: {mode.upper()}{rombel_info})...")

    # Siapkan styling standar
    font_standard = Font(name="Calibri", size=11, bold=False)
    thin_side = Side(style='thin', color='CCCCCC')
    cell_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    used_usernames = set()
    start_row = 7
    total_rows = start_row + count - 1

    date_format_str = r'[$-421]d\ mmmm\ yyyy'

    # Progress bar setup
    milestone = max(1, count // 20)

    for i in range(1, count + 1):
        row_num = start_row + i - 1
        student_data = generate_single_student(i, level, mode, used_usernames, rombel_input=rombel)

        for col_idx, val in enumerate(student_data, start=1):
            cell = ws.cell(row=row_num, column=col_idx)
            cell.font = font_standard
            cell.border = cell_border

            # Penanganan tipe data khusus
            if isinstance(val, datetime.datetime) or isinstance(val, datetime.date):
                cell.value = val
                cell.number_format = date_format_str
            elif col_idx in [6, 8, 11, 23, 35, 41, 47, 66]:  # NIS, NISN, NIK, HP, No. KK
                cell.value = str(val) if val is not None else None
                cell.number_format = '@'
            elif isinstance(val, int):
                cell.value = val
                cell.number_format = '0'
            else:
                cell.value = val

        if i % milestone == 0 or i == count:
            pct = (i / count) * 100
            bar = "#" * int(pct // 5) + "-" * (20 - int(pct // 5))
            sys.stdout.write(f"\r    [{bar}] {pct:5.1f}% ({i}/{count} siswa)")
            sys.stdout.flush()

    print("\n[+] Memperbarui aturan Data Validation (Dropdown Excel) sesuai jumlah baris baru...")
    # Update Data Validation ranges jika total baris melebihi batas default (1008)
    for dv in ws.data_validations.dataValidation:
        sqref_str = str(dv.sqref)
        # Jika terdapat referensi sampai baris 1008, ganti ke total_rows
        new_sqref = re.sub(r'1008\b', str(total_rows), sqref_str)
        # Juga tangani referensi pendek jika ada
        dv.sqref = new_sqref

    print(f"[+] Menyimpan workbook ke: {output_path} ...")
    wb.save(output_path)
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"[OK] Sukses! File berhasil dibuat ({file_size_mb:.2f} MB).")
    print(f"     Total Data Siswa: {count:,} siswa (Baris {start_row} s.d {total_rows})")

    return output_path


def interactive_prompt(default_template: str):
    """
    Mode interaktif jika script dijalankan tanpa argumen baris perintah.
    """
    print("=" * 65)
    print("   GENERATOR DATA SISWA FORMAT SIDIGS / MURID DAPODIK EXCEL")
    print("=" * 65)

    # 1. Jumlah siswa
    count_input = input(f"\n1. Masukkan jumlah siswa yang ingin digenerate [Default 1000]: ").strip()
    count = int(count_input) if count_input.isdigit() and int(count_input) > 0 else 1000

    # 2. Output filename
    default_out = f"hasil_siswa_{count}.xlsx"
    out_input = input(f"2. Nama file output Excel [Default: {default_out}]: ").strip()
    output_path = out_input if out_input else default_out

    # 3. Jenjang sekolah
    print("\n3. Pilih Jenjang Sekolah:")
    print("   [1] SMA  - Sekolah Menengah Atas (Umur ~15-18 tahun) [Default]")
    print("   [2] SMK  - Sekolah Menengah Kejuruan (Jurusan: RPL, TKJ, AKL, DKV, dll.)")
    print("   [3] SMP  - Sekolah Menengah Pertama (Umur ~12-15 tahun)")
    print("   [4] SD   - Sekolah Dasar (Umur ~6-12 tahun)")
    print("   [5] TK   - TK / PAUD (Umur ~4-6 tahun)")
    print("   [6] MA   - Madrasah Aliyah (Umur ~15-18 tahun)")
    print("   [7] MTs  - Madrasah Tsanawiyah (Umur ~12-15 tahun)")
    print("   [8] MI   - Madrasah Ibtidaiyah (Umur ~6-12 tahun)")
    print("   [9] SLB  - Sekolah Luar Biasa (Disertai kebutuhan khusus)")
    level_choice = input("   Pilihan [1-9 atau ketik SMA/SMK/SMP/SD/TK/dll]: ").strip()
    choice_map = {
        "1": "SMA", "2": "SMK", "3": "SMP", "4": "SD", "5": "TK",
        "6": "MA", "7": "MTS", "8": "MI", "9": "SLB"
    }
    level = choice_map.get(level_choice, normalize_jenjang(level_choice))

    # 4. Mode pengisian
    print("\n4. Pilih Mode Pengisian Kolom:")
    print("   [1] Standar Template (Data utama + NIS & NISN terisi, kelas opsional) [Default]")
    print("   [2] Lengkap / Full   (Mengisi semua kolom termasuk Alamat, No KK, Fisik BB/TB, dsb.)")
    mode_choice = input("   Pilihan [1/2]: ").strip()
    mode = "full" if mode_choice == "2" else "standard"

    # 5. Kelas / Rombel spesifik
    rombel_input = input("\n5. Tentukan Kelas / Rombel? [OPSIONAL - Tekan ENTER untuk mengosongkan / ketik misal: X-A, X-B]: ").strip()
    rombel = rombel_input if rombel_input else None

    return {
        "template": default_template,
        "output": output_path,
        "count": count,
        "level": level,
        "mode": mode,
        "rombel": rombel,
        "seed": None
    }


def main():
    parser = argparse.ArgumentParser(
        description="Program pembuat (generator) data dummy siswa format Sidigs Murid-Dapodik Excel hingga 1000+ data."
    )
    parser.add_argument("-n", "--count", type=int, default=None, help="Jumlah siswa yang akan digenerate (contoh: 1000, 1500, 2000)")
    parser.add_argument("-t", "--template", type=str, default="format sidigs murid-dapodik.xlsx", help="Path file template Excel")
    parser.add_argument("-o", "--output", type=str, default=None, help="Nama/path file output Excel")
    parser.add_argument("-l", "--level", "--jenjang", type=str, default="SMA", help="Jenjang sekolah: SMA, SMK, SMP, SD, TK, PAUD, MA, MTS, MI, SLB (default: SMA)")
    parser.add_argument("-m", "--mode", type=str, choices=["standard", "full"], default="standard", help="Mode pengisian: 'standard' (persis sample template) atau 'full' (lengkap termasuk NIS, NISN, dsb.)")
    parser.add_argument("-r", "--rombel", "--kelas", type=str, default=None, dest="rombel", help="Tentukan nama kelas/rombel (opsional, contoh: 'X-A' atau 'X-1, X-2, X-3')")
    parser.add_argument("-s", "--seed", type=int, default=None, help="Random seed untuk hasil yang deterministik")

    args = parser.parse_args()

    # Jika tidak ada parameter jumlah atau output yang diberikan, jalankan mode interaktif
    if args.count is None and args.output is None:
        params = interactive_prompt(args.template)
    else:
        count = args.count if args.count is not None else 1000
        output = args.output if args.output is not None else f"hasil_siswa_{count}.xlsx"
        params = {
            "template": args.template,
            "output": output,
            "count": count,
            "level": normalize_jenjang(args.level),
            "mode": args.mode,
            "rombel": args.rombel,
            "seed": args.seed
        }

    out_file = generate_siswa_excel(
        template_path=params["template"],
        output_path=params["output"],
        count=params["count"],
        level=params["level"],
        mode=params["mode"],
        rombel=params["rombel"],
        seed=params["seed"]
    )

    cfg = JENJANG_CONFIG.get(normalize_jenjang(params["level"]), JENJANG_CONFIG["SMA"])
    print("\n" + "=" * 65)
    print("   RINGKASAN DATA YANG BERHASIL DIGENERATE")
    print("=" * 65)
    print(f"File Output : {os.path.abspath(out_file)}")
    print(f"Jumlah Siswa: {params['count']:,}")
    print(f"Jenjang     : {cfg['nama']}")
    print(f"Mode        : {params['mode'].upper()}")
    if params.get('rombel'):
        print(f"Kelas/Rombel: {params['rombel']}")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
