"""
Dataset wilayah, kota, kode Kemendagri / Dukcapil, kelurahan, kecamatan, dan kode pos.
"""

import random

# Format: (Nama Kota, Kode Wilayah 6 digit Dukcapil, Kelurahan List, Kecamatan List, Kode Pos List)
KOTA_WILAYAH = [
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

STREET_NAMES = [
    "Melati", "Mawar", "Diponegoro", "Sudirman", "Gajah Mada", "Pahlawan",
    "Merdeka", "Imam Bonjol", "Ahmad Yani", "Kartini", "Hayam Wuruk", "Veteran"
]

DUSUN_NAMES = [
    "Krajan", "Kebon", "Duwet", "Kedung", "Sumber", "Tengah", "Santren", "Kunden"
]


def get_random_location() -> dict:
    """
    Menghasilkan data wilayah lengkap secara acak.
    """
    kota_info = random.choice(KOTA_WILAYAH)
    return {
        "tempat_lahir": kota_info[0],
        "wilayah_code": kota_info[1],
        "kelurahan": random.choice(kota_info[2]),
        "kecamatan": random.choice(kota_info[3]),
        "kode_pos": random.choice(kota_info[4]),
        "dusun": "-" if random.random() < 0.6 else f"Dusun {random.choice(DUSUN_NAMES)}",
        "alamat": f"Jl. {random.choice(STREET_NAMES)} No. {random.randint(1, 150)}",
        "rt": random.randint(1, 20),
        "rw": random.randint(1, 12)
    }
