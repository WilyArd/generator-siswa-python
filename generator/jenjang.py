"""
Konfigurasi dan normalisasi jenjang pendidikan sekolah Indonesia.
"""

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
    """
    Normalisasi input jenjang (case-insensitive & mendukung alias) ke kode standar.
    Contoh: 'smk' -> 'SMK', 'paud' -> 'TK', 'madrasah ibtidaiyah' -> 'MI'.
    """
    if not level_str:
        return "SMA"
    s = str(level_str).strip().upper()
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
