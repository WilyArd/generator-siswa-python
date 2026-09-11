"""
Konstanta dan daftar pilihan standar untuk atribut siswa dan orang tua.
Nilai-nilai ini disesuaikan dengan aturan validasi dropdown pada format Excel Sidigs.
"""

# Agama (disesuaikan dengan komposisi umum di Indonesia)
AGAMA_LIST = [
    "Islam", "Islam", "Islam", "Islam", "Islam", "Islam", "Islam", "Islam",
    "Kristen", "Katolik", "Hindu", "Buddha"
]

# Jenis tempat tinggal
JENIS_TINGGAL_LIST = [
    "Bersama orang tua", "ORANGTUA", "Bersama orang tua", "ORANGTUA", "Wali", "Kost"
]

# Alat transportasi (harus cocok dengan formula validasi dropdown Excel)
TRANSPORTASI_LIST = [
    "Jalan Kaki", "Sepeda", "Sepeda Motor", "Sepeda Motor", "Ojek", "Mobil Pribadi", "Lainnnya"
]

# Jenjang pendidikan orang tua (harus cocok dengan formula validasi dropdown Excel)
PENDIDIKAN_LIST = [
    "SD Sederajat", "SMP Sederajat", "SMA Sederajat", "SMA Sederajat",
    "S1 / D4", "S1 / D4", "D3", "D1", "S2"
]

# Pekerjaan ayah
PEKERJAAN_AYAH_LIST = [
    "Wiraswasta", "Karyawan Swasta", "PNS / Guru", "Buruh",
    "Pedagang", "Petani", "Sopir", "TNI / Polri", "Tukang Kayu / Bangunan"
]

# Pekerjaan ibu
PEKERJAAN_IBU_LIST = [
    "Ibu Rumah Tangga", "Ibu Rumah Tangga", "Ibu Rumah Tangga",
    "Karyawan Swasta", "Wiraswasta", "Pedagang", "PNS / Guru", "Buruh"
]

# Rentang penghasilan orang tua (harus cocok dengan formula validasi dropdown Excel)
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

# Prefix nomor HP operator seluler Indonesia
PREFIX_HP = [
    "0812", "0813", "0821", "0822",
    "0852", "0853", "0857", "0858",
    "0877", "0878", "0895", "0896"
]
