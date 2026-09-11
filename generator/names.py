"""
Kumpulan dataset nama khas Indonesia (tanpa gelar akademis) untuk siswa dan orang tua.
"""

import random

# Nama depan laki-laki
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

# Nama depan perempuan
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

# Nama belakang / marga / keluarga Indonesia
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


def generate_name(is_male: bool) -> tuple[str, str]:
    """
    Menghasilkan nama lengkap (2 atau 3 kata) dan nama panggilan yang sesuai gender.
    Returns:
        tuple (full_name, nama_panggilan)
    """
    first_name = random.choice(NAMA_DEPAN_LAKI if is_male else NAMA_DEPAN_PEREMPUAN)
    mid_or_last = random.choice(NAMA_BELAKANG)

    if random.random() < 0.4:
        third_name = random.choice(NAMA_BELAKANG)
        while third_name == mid_or_last:
            third_name = random.choice(NAMA_BELAKANG)
        full_name = f"{first_name} {mid_or_last} {third_name}"
    else:
        full_name = f"{first_name} {mid_or_last}"

    return full_name, first_name
