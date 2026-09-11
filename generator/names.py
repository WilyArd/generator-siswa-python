"""
Kumpulan dataset nama khas Indonesia (tanpa gelar akademis) untuk siswa dan orang tua.
Dataset mencakup nama-nama dari berbagai suku bangsa: Jawa, Sunda, Batak, Minang,
Bugis-Makassar, Melayu, Madura, Bali, Betawi, dan lainnya.
"""

import random

# ─────────────────────────────────────────────────────────────────────────────
# NAMA DEPAN LAKI-LAKI
# ─────────────────────────────────────────────────────────────────────────────
NAMA_DEPAN_LAKI = [
    # Umum / Islami
    "Muhammad", "Ahmad", "Abdullah", "Abdurrahman", "Fathur", "Khoirul", "Nur",
    "Miftah", "Zainul", "Hairul", "Syamsul", "Anwarul", "Khairul",
    # Populer modern
    "Dimas", "Rizky", "Kevin", "Arya", "Bayu", "Fadhil", "Bagus", "Ilham",
    "Farhan", "Aditya", "Rayhan", "Daffa", "Rio", "Aldo", "Gilang", "Fajar",
    "Rian", "Wahyu", "Yusuf", "Denis", "Rama", "Danu", "Rendy", "Reza",
    "Satria", "Iqbal", "Alif", "Haikal", "Tegar", "Bintang", "Galang",
    "Rifki", "Angga", "Doni", "Vicky", "Yoga", "Brian", "Naufal",
    "Zaki", "Dzaky", "Andre", "Fauzan", "Faisal",
    # Nama Jawa tradisional
    "Bambang", "Agus", "Budi", "Tri", "Joko", "Hadi", "Dwi", "Arif",
    "Agung", "Wahid", "Anwar", "Ridwan", "Lukman", "Rahmat", "Syahrul",
    "Taufik", "Eko", "Yanto", "Suryo", "Wawan", "Slamet", "Sutrisno",
    "Teguh", "Purwanto", "Triyono", "Samsul", "Subhan", "Mujib", "Riyadi",
    "Supriyadi", "Hartono", "Wahono", "Endro", "Gigih", "Gatot", "Danang",
    # Nama Sunda
    "Asep", "Dedi", "Ujang", "Ade", "Agep", "Cecep", "Dadang", "Endang",
    "Iwan", "Oman", "Tatang", "Yayan", "Hendra", "Opik", "Usep", "Dudung",
    "Encep", "Ajat", "Dani", "Sofyan", "Wahyu", "Ridho",
    # Nama Batak
    "Parlin", "Hotman", "Jonatan", "Binsar", "Haposan", "Togar", "Horasman",
    "Martua", "Royke", "Timbul", "Parsaoran", "Rikky", "Mauliate", "Bonar",
    "Nixon", "Janri", "Jekson", "Sihol", "Hendro",
    # Nama Minang
    "Darmawan", "Fahreza", "Hafiz", "Khairul", "Ridho", "Zulhafnur",
    "Mukhlis", "Fajri", "Aziz", "Roni", "Safrizal", "Yogi", "Hendra",
    "Irfan", "Teguh", "Hendri", "Amri", "Fakrul", "Gusri",
    # Nama Bugis-Makassar
    "Andi", "Asrul", "Hasrul", "Syamsir", "Amirul", "Muh", "Arifuddin",
    "Kamaruddin", "Syahril", "Muhaimin", "Alimuddin", "Mursalim", "Hasbullah",
    "Samsuddin", "Tamrin", "Erwin", "Nurfajar", "Suhardi", "Rusdi",
    # Nama Melayu / Kalimantan
    "Syarifuddin", "Zulkifli", "Hairul", "Firdaus", "Samsul", "Syafrudin",
    "Mursid", "Azhar", "Fakhrul", "Hafidz", "Mukhtar", "Saepul",
    # Nama Bali / NTT / NTB
    "Ketut", "Nyoman", "Wayan", "Made", "Putu", "Gede", "Kadek", "Komang",
    "Ngurah", "Dewa", "Lalu", "Hamdi", "Imran", "Haerul",
    # Nama Madura
    "Zainullah", "Fathorrozi", "Syaifullah", "Moh", "Abd", "Suprayitno",
    "Khoiron", "Badrus", "Habibi", "Miftahul",
    # Tambahan populer
    "Arga", "Rendra", "Farid", "Ghafi", "Kurnia", "Mahendra", "Pandu",
    "Raffi", "Sultan", "Tirta", "Vino", "Wisnu", "Zidan", "Akbar",
    "Bilal", "Candra", "Fikri", "Giri", "Haris", "Julian", "Latif",
    "Maulana", "Noval", "Oki", "Panji", "Rasyid", "Sandi", "Tomi", "Wildan",
    "Aflah", "Azzam", "Falih", "Ghilman", "Hamdani", "Kamil", "Nabil",
    "Qodir", "Salim", "Tholib", "Umar", "Wafiq", "Yahya", "Zidan",
]

# ─────────────────────────────────────────────────────────────────────────────
# NAMA DEPAN PEREMPUAN
# ─────────────────────────────────────────────────────────────────────────────
NAMA_DEPAN_PEREMPUAN = [
    # Umum / Islami
    "Siti", "Nur", "Nurul", "Anisa", "Annisa", "Aisyah", "Khadijah", "Fatimah",
    "Maryam", "Rohmah", "Nuraini", "Zulaikha", "Hasanah", "Latifah", "Rahmah",
    "Fitriah", "Fauziah", "Jamilah", "Badriyah", "Humaira", "Ulfah", "Amanah",
    # Populer modern
    "Nabila", "Putri", "Zahra", "Aulia", "Tiara", "Dewi", "Indah", "Maya",
    "Rina", "Salma", "Fitri", "Amanda", "Bella", "Cindy", "Dinda", "Eka",
    "Farah", "Gita", "Hana", "Intan", "Jessica", "Karina", "Lestari",
    "Melani", "Nadia", "Olivia", "Pratiwi", "Rahma", "Safira", "Tasya",
    "Ulfa", "Vina", "Wulan", "Yasmin", "Zaskia", "Cantika", "Clarissa",
    "Syifa", "Nayla", "Alya", "Ayu", "Desi", "Erna", "Fani", "Gisella",
    "Hesti", "Ika", "Juwita", "Kania", "Lia", "Mega", "Novita", "Oktavia",
    "Poppy", "Rania", "Siska", "Tari", "Utari", "Vivi", "Winda", "Yulia",
    "Adelia", "Balqis", "Chelsea", "Dhea", "Elvira", "Fadila", "Ghina",
    "Halimah", "Kamila", "Laras", "Mutia", "Nadira",
    # Nama Jawa tradisional
    "Sri", "Endah", "Rini", "Wati", "Yuni", "Ningsih", "Astuti", "Wahyuni",
    "Rahayu", "Sulistyowati", "Murniati", "Retno", "Supriyati", "Dwiyanti",
    "Triyanti", "Suharti", "Pujiastuti", "Handayani", "Widyastuti", "Purwati",
    "Sulastri", "Martini", "Asih", "Hartati", "Sumiyati", "Sriatun",
    # Nama Sunda
    "Ai", "Neng", "Cicih", "Dedeh", "Elis", "Entin", "Ida", "Leni",
    "Nani", "Nining", "Sari", "Teti", "Yayah", "Cucu", "Enok",
    "Rosmawati", "Dedeh", "Neneng", "Lisnawati", "Imas",
    # Nama Batak
    "Hotmaida", "Natalina", "Rotua", "Marianna", "Doris", "Elfrida",
    "Lestari", "Rohani", "Tiarma", "Veronika", "Yolanda", "Hanna",
    "Margareta", "Rosinta", "Berliana", "Friska",
    # Nama Minang
    "Rahmi", "Sari", "Rini", "Yosi", "Nisa", "Suci", "Dwi",
    "Meli", "Fenty", "Resty", "Rika", "Icha", "Yola", "Elva",
    "Bunga", "Mayang", "Sartika", "Reza", "Mita", "Putri",
    # Nama Bugis-Makassar
    "Andi", "Hasnah", "Nuraeni", "Sumarni", "Salmiah", "Rosmini",
    "Hajriani", "Musriani", "Wahidah", "Suryani", "Muliani", "Hasriani",
    "Reski", "Risna", "Nurwahida",
    # Nama Melayu / Kalimantan
    "Rohana", "Zulaikha", "Salmah", "Masitah", "Halijah", "Ramlah",
    "Mariam", "Nor", "Norsyahida", "Hayati", "Rohayati",
    # Nama Bali / NTT / NTB
    "Ketut", "Nyoman", "Wayan", "Made", "Putu", "Kadek", "Komang",
    "Dewi", "Sri", "Luh", "Baiq", "Dewa", "Ni", "Ayu",
    # Tambahan yang populer
    "Zulfa", "Qonita", "Chandra", "Chantika", "Keisya", "Keisha",
    "Kinasih", "Kalika", "Anindya", "Azzahra", "Raisya", "Khanza",
    "Khayla", "Naura", "Nayra", "Aaliya", "Adinda", "Afifah", "Akila",
    "Amara", "Ardelia", "Arifa", "Ariva", "Aufa", "Azka", "Azkia",
    "Callista", "Davina", "Delvina", "Elviana", "Falisha", "Fira",
    "Galuh", "Garnis", "Hikmah", "Husna", "Iqrima", "Irene",
    "Janneta", "Jasmine", "Kayla", "Kezia", "Khairina", "Lailatul",
    "Liana", "Liviya", "Malika", "Marsya", "Meylan", "Mirza",
    "Nafisah", "Nailah", "Nayli", "Nisa", "Nisrina", "Nurazizah",
    "Rachelia", "Radina", "Raisya", "Rara", "Rasya", "Reifani",
    "Salmaa", "Samira", "Saskia", "Savira", "Shafira", "Shakila",
    "Tania", "Tessa", "Tifa", "Tsabita", "Vanessa", "Vidya",
    "Viola", "Virda", "Wilma", "Wiwit", "Yolanda",
]

# ─────────────────────────────────────────────────────────────────────────────
# NAMA BELAKANG / MARGA / KELUARGA
# ─────────────────────────────────────────────────────────────────────────────
NAMA_BELAKANG = [
    # Umum / Jawa Tengah - Jawa Timur
    "Pratama", "Saputra", "Hidayat", "Santoso", "Wibowo", "Setiawan", "Wijaya",
    "Kusuma", "Utomo", "Nugroho", "Lestari", "Ramadhan", "Firmansyah",
    "Prasetyo", "Kurniawan", "Mahendra", "Subagyo", "Suherman", "Suryanto",
    "Priyanto", "Budiman", "Gunawan", "Wardhana", "Darmawan", "Wahyudi",
    "Yulianto", "Sucipto", "Purnama", "Kurnia", "Alamsyah", "Sudirman",
    "Hartono", "Permana", "Santosa", "Wicaksono", "Supriadi", "Supriyatno",
    "Purwanto", "Suharto", "Sunaryo", "Triyono", "Wahyono", "Mulyono",
    "Susanto", "Bambang", "Prayogo", "Yudiantoro", "Krisnawan", "Harianto",
    "Andrianto", "Sulistyawan", "Budiyanto", "Kuswanto", "Suwardi", "Rudiyanto",
    "Nuryanto", "Sugiarto", "Haryono", "Suyatno", "Subagya", "Purnomo",
    "Kusumanto", "Widjaja", "Salim", "Soekarno", "Mulyadi", "Hadianto",
    "Haryadi", "Suroto", "Mardiyanto", "Nuryadi", "Kusnadi", "Irawan",
    "Sukarno", "Sudrajat", "Supartono", "Widodo", "Atmojo", "Soekarjo",
    # Sunda
    "Sopandi", "Suherman", "Suhendar", "Supardi", "Suryana", "Supriatna",
    "Rosmana", "Permana", "Mulyana", "Hidayat", "Rustaman", "Somantri",
    "Sudrajat", "Iskandar", "Hamdani", "Rahmat", "Firman", "Sobarna",
    # Batak Toba
    "Siregar", "Nasution", "Hasibuan", "Harahap", "Batubara", "Pasaribu",
    "Simanjuntak", "Hutapea", "Panjaitan", "Manurung", "Sinaga", "Siahaan",
    "Napitupulu", "Situmorang", "Purba", "Saragih", "Hutabarat", "Panggabean",
    "Tobing", "Sibuea", "Silalahi", "Pardede", "Tampubolon", "Simarmata",
    "Sigalingging", "Sibarani", "Sirait", "Simbolon", "Sihotang", "Sianturi",
    "Samosir", "Rajagukguk", "Nainggolan", "Manik", "Lumban Batu",
    # Batak Karo
    "Ginting", "Tarigan", "Sembiring", "Brahmana", "Perangin-angin", "Karo-karo",
    "Bangun", "Barus", "Sinulingga", "Sitepu", "Milala", "Gurusinga",
    # Minangkabau
    "Chaniago", "Piliang", "Koto", "Sikumbang", "Melayu", "Tanjung",
    "Lubis", "Daulay", "Hakim", "Fauzi", "Munandar", "Mustofa",
    "Dt. Bagindo", "Pane", "Jambak", "Mandahiling", "Ganting", "Caniago",
    "Sutan", "Rajo", "Datuk", "Rangkayo", "Tuanku",
    # Bugis-Makassar
    "Andi", "Karaeng", "Dg.", "Petta", "Puang",
    "Mappaselling", "Lewa", "Wahab", "Jamaluddin", "Amiruddin",
    "Kamaluddin", "Syamsuddin", "Alimuddin", "Nurdin", "Hasanuddin",
    "Mattulada", "Daeng", "Palallo", "Latief", "Makka",
    # Melayu / Kalimantan
    "Syarifuddin", "Zulkifli", "Sulaiman", "Iskandar", "Nawawi", "Hamid",
    "Rahman", "Rahim", "Hamdan", "Hamzah", "Yahya", "Ibrahim", "Harun",
    "Khalid", "Idris", "Yusoff", "Abdullah", "Abdillah",
    # Bali
    "Wayan", "Made", "Nyoman", "Ketut", "Putu", "Gede", "Kadek",
    "Rai", "Suardika", "Widiasa", "Artana", "Suarjana", "Wirawan",
    "Susanta", "Widana", "Sudana", "Karma", "Budiasa", "Suastika",
    # Flores / NTT
    "Moa", "Fernandez", "da Costa", "de Jesus", "Kleden", "Naikofi",
    "Bria", "Labi", "Leran", "Sogen", "Tukan", "Boli",
    # Ambon / Maluku
    "Pattimura", "Latumahina", "Manuputty", "Alfons", "Tuasikal", "Laisow",
    "Uneputty", "Salakay", "Amahorseya", "Siahaya", "Pello", "Pelupessy",
    # Sulawesi / Minahasa
    "Roring", "Mandagi", "Runtuwene", "Mamahit", "Siwi", "Tuuk",
    "Rompis", "Sumendap", "Worang", "Lolong", "Talumepa", "Korengkeng",
    # Jawa Barat Priangan
    "Suryana", "Sopandi", "Sukarta", "Sukarya", "Suhara", "Sujana",
    "Sutarya", "Somadikarta", "Partawijaya", "Suparman", "Supatman",
    # Tambahan umum
    "Putera", "Putra", "Puteri", "Kusumah", "Pradana", "Arifin",
    "Firdaus", "Zulkarnaen", "Dermawan", "Irfansyah", "Budiyono",
    "Setiyono", "Hermawan", "Handoyo", "Cahyono", "Wahyono",
    "Baskoro", "Hakim", "Putu", "Fatah", "Yusri", "Bahri",
]

# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI PEMBANGKIT NAMA
# ─────────────────────────────────────────────────────────────────────────────

# Nama depan dua kata yang lazim dipakai bersamaan (compound first names)
NAMA_DEPAN_COMPOUND_LAKI = [
    ("Muhammad", "Rizky"), ("Muhammad", "Fathur"), ("Muhammad", "Alif"),
    ("Muhammad", "Ilham"), ("Muhammad", "Farhan"), ("Muhammad", "Fadly"),
    ("Muhammad", "Naufal"), ("Muhammad", "Zidan"), ("Muhammad", "Rayhan"),
    ("Muhammad", "Iqbal"), ("Ahmad", "Fadhil"), ("Ahmad", "Muzakki"),
    ("Ahmad", "Rifai"), ("Nur", "Ahmad"), ("Nur", "Wahyu"), ("Nur", "Hasan"),
    ("Abdul", "Aziz"), ("Abdul", "Rahman"), ("Abdul", "Ghafur"),
    ("Abdurrahman", "Wahid"), ("Khairul", "Anwar"), ("Maulana", "Yusuf"),
]

NAMA_DEPAN_COMPOUND_PEREMPUAN = [
    ("Siti", "Nurhaliza"), ("Siti", "Aisyah"), ("Siti", "Maryam"),
    ("Siti", "Rahma"), ("Nur", "Aisyah"), ("Nur", "Safira"),
    ("Nur", "Azizah"), ("Nurul", "Hidayah"), ("Nurul", "Aini"),
    ("Nurul", "Huda"), ("Umi", "Kalsum"), ("Dewi", "Larasati"),
    ("Putri", "Ayu"), ("Putri", "Kusuma"), ("Tri", "Wahyuni"),
    ("Dwi", "Lestari"), ("Sri", "Wahyuni"), ("Sri", "Rahayu"),
    ("Sri", "Rejeki"), ("Dian", "Wahyuni"), ("Dian", "Ayu"),
]


def generate_name(is_male: bool) -> tuple[str, str]:
    """
    Menghasilkan nama lengkap (2 atau 3 kata) dan nama panggilan yang sesuai gender.

    Variasi:
    - 15%: Nama depan compound (misal "Muhammad Rizky Saputra")
    - 40%: Nama depan + tengah + belakang (3 kata)
    - 45%: Nama depan + belakang (2 kata)

    Returns:
        tuple (full_name, nama_panggilan)
    """
    compound_pool = NAMA_DEPAN_COMPOUND_LAKI if is_male else NAMA_DEPAN_COMPOUND_PEREMPUAN
    first_pool = NAMA_DEPAN_LAKI if is_male else NAMA_DEPAN_PEREMPUAN

    roll = random.random()

    if roll < 0.15:
        # Nama compound sebagai nama depan, lalu tambahkan nama belakang
        compound = random.choice(compound_pool)
        last_name = random.choice(NAMA_BELAKANG)
        full_name = f"{compound[0]} {compound[1]} {last_name}"
        panggilan = compound[1]  # nama tengah sebagai panggilan
    elif roll < 0.50:
        # 3 kata: nama depan + tengah (belakang) + belakang kedua
        first_name = random.choice(first_pool)
        mid_name = random.choice(NAMA_BELAKANG)
        last_name = random.choice(NAMA_BELAKANG)
        while last_name == mid_name:
            last_name = random.choice(NAMA_BELAKANG)
        full_name = f"{first_name} {mid_name} {last_name}"
        panggilan = first_name
    else:
        # 2 kata: nama depan + belakang
        first_name = random.choice(first_pool)
        last_name = random.choice(NAMA_BELAKANG)
        full_name = f"{first_name} {last_name}"
        panggilan = first_name

    return full_name, panggilan
