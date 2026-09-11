"""
Logika pembentukan data siswa lengkap (72 kolom) untuk format Excel Sidigs Dapodik.
"""

import re
import random
import datetime

from generator.constants import (
    AGAMA_LIST, JENIS_TINGGAL_LIST, TRANSPORTASI_LIST,
    PENDIDIKAN_LIST, PEKERJAAN_AYAH_LIST, PEKERJAAN_IBU_LIST,
    PENGHASILAN_LIST, PREFIX_HP
)
from generator.names import generate_name, NAMA_DEPAN_LAKI, NAMA_DEPAN_PEREMPUAN, NAMA_BELAKANG
from generator.locations import get_random_location
from generator.jenjang import JENJANG_CONFIG, normalize_jenjang


def clean_username(text: str) -> str:
    """Mengubah teks nama menjadi username huruf kecil tanpa spasi dan karakter khusus."""
    clean = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return clean[:20] if len(clean) > 20 else clean


def generate_nik(wilayah_code: str, tgl: int, bln: int, thn: int, is_female: bool, urut: int) -> str:
    """
    Menghasilkan 16 digit NIK Indonesia yang realistis sesuai standar Kemendagri / Dukcapil:
    - 6 digit kode wilayah (Provinsi + Kab/Kota + Kec)
    - 2 digit tanggal (khusus perempuan: tanggal + 40)
    - 2 digit bulan
    - 2 digit tahun (2 digit terakhir)
    - 4 digit nomor urut unik
    """
    dd = tgl + 40 if is_female else tgl
    yy = thn % 100
    serial = (urut % 9999) + 1
    return f"{wilayah_code}{dd:02d}{bln:02d}{yy:02d}{serial:04d}"


def generate_single_student(idx: int, level: str, mode: str, used_usernames: set, rombel_input: str = None) -> list:
    """
    Menghasilkan data lengkap 1 siswa (list 72 elemen) yang siap dimasukkan ke baris Excel Sidigs Dapodik.

    Args:
        idx: Nomor urut siswa (1, 2, 3, ...)
        level: Jenjang sekolah (SMA, SMK, SMP, SD, TK, dsb.)
        mode: Mode pengisian ('standard' atau 'full')
        used_usernames: Set kumpulan username yang sudah terpakai agar unik
        rombel_input: Opsi string kelas/rombel yang ditentukan pengguna (opsional)

    Returns:
        list berisi 72 nilai kolom sesuai urutan template Sidigs
    """
    cfg = JENJANG_CONFIG.get(normalize_jenjang(level), JENJANG_CONFIG["SMA"])

    # 1. Gender & Nama
    is_male = (idx % 2 == 1) if random.random() < 0.9 else (random.choice([True, False]))
    jenis_kelamin = "Laki - Laki" if is_male else "Perempuan"
    full_name, nama_panggilan = generate_name(is_male)

    # 2. Username & Password Murid (unik tanpa spasi)
    base_user = clean_username(full_name)
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

    # 4. Tanggal Lahir Siswa (disesuaikan dengan jenjang)
    curr_year = datetime.datetime.now().year
    birth_year = random.randint(curr_year - cfg["max_age"], curr_year - cfg["min_age"])
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    tgl_lahir_siswa = datetime.datetime(birth_year, birth_month, birth_day, 0, 0)

    # 5. Wilayah & NIK Siswa
    loc = get_random_location()
    tempat_lahir = loc["tempat_lahir"]
    wilayah_code = loc["wilayah_code"]
    kelurahan = loc["kelurahan"]
    kecamatan = loc["kecamatan"]
    kode_pos = loc["kode_pos"]
    dusun = loc["dusun"]
    alamat = loc["alamat"]
    rt = loc["rt"]
    rw = loc["rw"]

    nik_siswa = generate_nik(wilayah_code, birth_day, birth_month, birth_year, not is_male, idx)

    # 6. Kontak & Atribut Siswa
    hp_prefix = random.choice(PREFIX_HP)
    hp_suffix = f"{random.randint(10000000, 99999999):08d}"
    hp = f"{hp_prefix}{hp_suffix}"

    agama = random.choice(AGAMA_LIST)
    jenis_tinggal = random.choice(JENIS_TINGGAL_LIST)
    alat_transportasi = random.choice(TRANSPORTASI_LIST)

    # 7. Data Orang Tua (Ayah & Ibu)
    # Data Ayah
    ayah_first = random.choice(NAMA_DEPAN_LAKI)
    ayah_last = random.choice(NAMA_BELAKANG)
    nama_ayah = f"{ayah_first} {ayah_last}".upper() if random.random() < 0.5 else f"{ayah_first} {ayah_last}"
    ayah_birth_year = birth_year - random.randint(25, 36)
    ayah_tgl_lahir = datetime.datetime(ayah_birth_year, random.randint(1, 12), random.randint(1, 28), 0, 0)
    ayah_pendidikan = random.choice(PENDIDIKAN_LIST)
    ayah_pekerjaan = random.choice(PEKERJAAN_AYAH_LIST)
    ayah_penghasilan = random.choice(PENGHASILAN_LIST)
    ayah_nik = generate_nik(wilayah_code, ayah_tgl_lahir.day, ayah_tgl_lahir.month, ayah_birth_year, False, idx + 1000)

    # Data Ibu
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
    row_values = [
        idx,                                 # Col 1 (A): No
        full_name,                           # Col 2 (B): Nama (*)
        nama_panggilan,                      # Col 3 (C): Nama Panggilan
        username,                            # Col 4 (D): Username Login Murid
        password,                            # Col 5 (E): Password Login Murid
        nis,                                 # Col 6 (F): NIS
        jenis_kelamin,                       # Col 7 (G): Jenis Kelamin (*)
        nisn,                                # Col 8 (H): NISN
        tempat_lahir,                        # Col 9 (I): Tempat Lahir (*)
        tgl_lahir_siswa,                     # Col 10 (J): Tanggal Lahir (*)
        nik_siswa,                           # Col 11 (K): NIK
        agama,                               # Col 12 (L): Agama
        alamat if mode == "full" else None,  # Col 13 (M): Alamat
        rt,                                  # Col 14 (N): RT
        rw,                                  # Col 15 (O): RW
        dusun,                               # Col 16 (P): Dusun
        kelurahan,                           # Col 17 (Q): Kelurahan
        kecamatan,                           # Col 18 (R): Kecamatan
        kode_pos,                            # Col 19 (S): Kode Pos
        jenis_tinggal,                       # Col 20 (T): Jenis Tinggal
        alat_transportasi,                   # Col 21 (U): Alat Transportasi
        "-",                                 # Col 22 (V): Telepon
        hp,                                  # Col 23 (W): HP
        "-",                                 # Col 24 (X): Email
        "-",                                 # Col 25 (Y): SKHUN
        "Tidak",                             # Col 26 (Z): Penerima KPS
        "-",                                 # Col 27 (AA): No. KPS
        username_wali,                       # Col 28 (AB): Username Login Walimurid
        password_wali,                       # Col 29 (AC): Password Login Walimurid
        nama_ayah,                           # Col 30 (AD): Data Ayah - Nama
        ayah_tgl_lahir,                      # Col 31 (AE): Data Ayah - Tanggal Lahir (*)
        ayah_pendidikan,                     # Col 32 (AF): Data Ayah - Jenjang Pendidikan
        ayah_pekerjaan if mode == "full" else None,  # Col 33 (AG): Pekerjaan
        ayah_penghasilan,                    # Col 34 (AH): Penghasilan
        ayah_nik if mode == "full" else None,        # Col 35 (AI): NIK Ayah
        nama_ibu,                            # Col 36 (AJ): Data Ibu - Nama
        ibu_tgl_lahir,                       # Col 37 (AK): Data Ibu - Tanggal Lahir (*)
        ibu_pendidikan,                      # Col 38 (AL): Data Ibu - Jenjang Pendidikan
        ibu_pekerjaan if mode == "full" else None,   # Col 39 (AM): Pekerjaan
        ibu_penghasilan,                     # Col 40 (AN): Penghasilan
        ibu_nik if mode == "full" else None,         # Col 41 (AO): NIK Ibu
        None,                                # Col 42 (AP): Data Wali - Nama
        None,                                # Col 43 (AQ): Tanggal Lahir Wali
        None,                                # Col 44 (AR): Jenjang Pendidikan Wali
        None,                                # Col 45 (AS): Pekerjaan Wali
        None,                                # Col 46 (AT): Penghasilan Wali
        None,                                # Col 47 (AU): NIK Wali
        rombel,                              # Col 48 (AV): Rombel Saat Ini
        None,                                # Col 49 (AW): Nomor Peserta UN
        None,                                # Col 50 (AX): Nomor Seri Ijazah
        "Tidak" if mode == "full" else None, # Col 51 (AY): Penerima KIP
        None,                                # Col 52 (AZ): Nomor KIP
        None,                                # Col 53 (BA): Nama Di KIP
        None,                                # Col 54 (BB): Nomor KKS
        None,                                # Col 55 (BC): No Registrasi Akta Lahir
        None,                                # Col 56 (BD): Bank
        None,                                # Col 57 (BE): Nomor Rekening Bank
        None,                                # Col 58 (BF): Rekening Atas Nama
        None,                                # Col 59 (BG): Layak PIP
        None,                                # Col 60 (BH): Alasan Layak PIP
        kebutuhan_khusus,                    # Col 61 (BI): Kebutuhan Khusus
        sekolah_asal,                        # Col 62 (BJ): Sekolah Asal
        anak_ke,                             # Col 63 (BK): Anak Ke Berapa
        None,                                # Col 64 (BL): Lintang
        None,                                # Col 65 (BM): Bujur
        no_kk,                               # Col 66 (BN): No. KK
        bb,                                  # Col 67 (BO): Berat Badan
        tb,                                  # Col 68 (BP): Tinggi Badan
        None,                                # Col 69 (BQ): Lingkar Kepala
        jml_saudara,                         # Col 70 (BR): Jml. Saudara Kandung
        jarak_km,                            # Col 71 (BS): Jarak Rumah ke Sekolah
        None                                 # Col 72 (BT): Nomor Virtual Account
    ]

    return row_values
