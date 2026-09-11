"""
Dataset wilayah, kota, kode Kemendagri / Dukcapil, kelurahan, kecamatan, dan kode pos.
Mencakup kota dan kabupaten dari seluruh provinsi di Indonesia.

Format tuple: (Nama Kota/Kab, Kode Wilayah 6 digit Dukcapil, List Kelurahan, List Kecamatan, List Kode Pos)
Kode Wilayah: [2 digit Provinsi][2 digit Kab/Kota][2 digit Kecamatan]
"""

import random

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI ACEH (11)
# ─────────────────────────────────────────────────────────────────────────────
_ACEH = [
    ("Banda Aceh", "117101",
     ["Baiturrahman", "Kuta Alam", "Ulee Kareng", "Syiah Kuala", "Meuraxa", "Kutaraja"],
     ["Baiturrahman", "Kuta Alam", "Ulee Kareng", "Syiah Kuala", "Meuraxa"],
     [23111, 23121, 23124, 23116, 23115]),
    ("Lhokseumawe", "117201",
     ["Banda Sakti", "Muara Dua", "Blang Mangat", "Muara Satu"],
     ["Banda Sakti", "Muara Dua", "Blang Mangat"],
     [24351, 24352, 24356, 24371]),
    ("Langsa", "117301",
     ["Langsa Kota", "Langsa Baro", "Langsa Barat", "Langsa Lama", "Langsa Timur"],
     ["Langsa Kota", "Langsa Baro", "Langsa Barat"],
     [24412, 24415, 24416]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SUMATERA UTARA (12)
# ─────────────────────────────────────────────────────────────────────────────
_SUMUT = [
    ("Medan", "127101",
     ["Medan Kota", "Medan Baru", "Medan Timur", "Medan Sunggal", "Medan Selayang",
      "Medan Tuntungan", "Medan Marelan", "Medan Helvetia", "Medan Labuhan",
      "Pulo Brayan Bengkel", "Tanjung Mulia", "Belawan Bahari", "Amplas"],
     ["Medan Kota", "Medan Baru", "Medan Timur", "Medan Sunggal", "Medan Petisah",
      "Medan Selayang", "Medan Tuntungan", "Medan Helvetia", "Medan Marelan",
      "Medan Belawan", "Medan Barat", "Medan Johor"],
     [20111, 20151, 20236, 20122, 20116, 20142, 20255, 20123]),
    ("Binjai", "127201",
     ["Binjai Kota", "Binjai Selatan", "Binjai Timur", "Binjai Utara", "Binjai Barat"],
     ["Binjai Kota", "Binjai Selatan", "Binjai Timur", "Binjai Utara"],
     [20711, 20723, 20742, 20752, 20742]),
    ("Pematang Siantar", "127301",
     ["Siantar Utara", "Siantar Timur", "Siantar Selatan", "Siantar Barat", "Siantar Marihat"],
     ["Siantar Utara", "Siantar Timur", "Siantar Selatan", "Siantar Barat"],
     [21111, 21141, 21155, 21163, 21175]),
    ("Tebing Tinggi", "127401",
     ["Padang Hulu", "Rambutan", "Padang Hilir", "Tebing Tinggi Kota", "Bajenis"],
     ["Padang Hulu", "Rambutan", "Padang Hilir", "Tebing Tinggi Kota"],
     [20611, 20623, 20632, 20636]),
    ("Deli Serdang", "120401",
     ["Sunggal", "Medan Deli", "Patumbak", "Lubuk Pakam", "Pancur Batu", "Percut Sei Tuan"],
     ["Sunggal", "Patumbak", "Lubuk Pakam", "Pancur Batu", "Percut Sei Tuan"],
     [20351, 20363, 20516, 20353, 20371]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SUMATERA BARAT (13)
# ─────────────────────────────────────────────────────────────────────────────
_SUMBAR = [
    ("Padang", "137101",
     ["Padang Utara", "Padang Barat", "Padang Timur", "Padang Selatan", "Nanggalo",
      "Kuranji", "Pauh", "Lubuk Kilangan", "Lubuk Begalung", "Bungus Teluk Kabung",
      "Indarung", "Tabing", "Ulak Karang"],
     ["Padang Utara", "Padang Barat", "Padang Timur", "Padang Selatan",
      "Nanggalo", "Kuranji", "Pauh", "Lubuk Kilangan", "Lubuk Begalung"],
     [25111, 25117, 25128, 25133, 25141, 25157, 25175, 25224, 25221]),
    ("Padang Panjang", "137201",
     ["Padang Panjang Barat", "Padang Panjang Timur", "Bukit Surungan"],
     ["Padang Panjang Barat", "Padang Panjang Timur"],
     [27111, 27112, 27113]),
    ("Bukittinggi", "137301",
     ["Aur Birugo Tigo Baleh", "Guguk Panjang", "Mandiangin Koto Selayan"],
     ["Aur Birugo Tigo Baleh", "Guguk Panjang", "Mandiangin Koto Selayan"],
     [26111, 26116, 26131]),
    ("Payakumbuh", "137401",
     ["Payakumbuh Barat", "Payakumbuh Timur", "Payakumbuh Utara", "Payakumbuh Selatan"],
     ["Payakumbuh Barat", "Payakumbuh Timur", "Payakumbuh Utara"],
     [26211, 26218, 26225]),
    ("Solok", "137501",
     ["Lubuk Sikarah", "Tanjung Harapan"],
     ["Lubuk Sikarah", "Tanjung Harapan"],
     [27311, 27322]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI RIAU (14)
# ─────────────────────────────────────────────────────────────────────────────
_RIAU = [
    ("Pekanbaru", "147101",
     ["Tampan", "Binawidya", "Payung Sekaki", "Marpoyan Damai", "Bukit Raya",
      "Lima Puluh", "Pekanbaru Kota", "Sail", "Rumbai", "Rumbai Pesisir",
      "Senapelan", "Sukajadi", "Tenayan Raya"],
     ["Tampan", "Payung Sekaki", "Marpoyan Damai", "Bukit Raya",
      "Lima Puluh", "Pekanbaru Kota", "Rumbai", "Senapelan", "Sukajadi"],
     [28291, 28152, 28128, 28125, 28113, 28112, 28265, 28153, 28124]),
    ("Dumai", "147201",
     ["Dumai Kota", "Dumai Barat", "Dumai Timur", "Bukit Kapur", "Medang Kampai"],
     ["Dumai Kota", "Dumai Barat", "Dumai Timur", "Bukit Kapur"],
     [28813, 28816, 28822, 28832]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI KEPULAUAN RIAU (21)
# ─────────────────────────────────────────────────────────────────────────────
_KEPRI = [
    ("Batam", "217101",
     ["Batam Kota", "Lubuk Baja", "Nongsa", "Batu Aji", "Sagulung", "Sei Beduk",
      "Bengkong", "Batu Ampar", "Belakang Padang", "Bulang", "Galang"],
     ["Batam Kota", "Lubuk Baja", "Nongsa", "Batu Aji", "Sagulung", "Sei Beduk"],
     [29444, 29434, 29436, 29423, 29437, 29435]),
    ("Tanjung Pinang", "217201",
     ["Tanjungpinang Kota", "Tanjungpinang Barat", "Tanjungpinang Timur", "Bukit Bestari"],
     ["Tanjungpinang Kota", "Tanjungpinang Barat", "Tanjungpinang Timur"],
     [29111, 29122, 29124, 29126]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI JAMBI (15)
# ─────────────────────────────────────────────────────────────────────────────
_JAMBI = [
    ("Jambi", "157101",
     ["Pasar Jambi", "Pelayangan", "Danau Sipin", "Telanaipura", "Jambi Selatan",
      "Jambi Timur", "Kota Baru", "Jelutung", "Alam Barajo", "Danau Teluk"],
     ["Pasar Jambi", "Telanaipura", "Jambi Selatan", "Jambi Timur", "Kota Baru",
      "Jelutung", "Alam Barajo"],
     [36111, 36122, 36135, 36143, 36133, 36137, 36361]),
    ("Sungai Penuh", "157201",
     ["Hamparan Rawang", "Sungai Penuh", "Tanah Kampung", "Kumun Debai", "Pesisir Bukit"],
     ["Hamparan Rawang", "Sungai Penuh", "Tanah Kampung"],
     [37111, 37115, 37116]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SUMATERA SELATAN (16)
# ─────────────────────────────────────────────────────────────────────────────
_SUMSEL = [
    ("Palembang", "167101",
     ["Ilir Barat I", "Ilir Barat II", "Ilir Timur I", "Ilir Timur II", "Kemuning",
      "Bukit Kecil", "Gandus", "Kalidoni", "Kertapati", "Plaju",
      "Sako", "Seberang Ulu I", "Seberang Ulu II", "Alang-alang Lebar", "Sematang Borang"],
     ["Ilir Barat I", "Ilir Barat II", "Ilir Timur I", "Ilir Timur II",
      "Kemuning", "Bukit Kecil", "Gandus", "Kalidoni", "Kertapati", "Plaju"],
     [30111, 30152, 30121, 30172, 30151, 30135, 30152, 30161, 30258, 30267]),
    ("Prabumulih", "167201",
     ["Prabumulih Barat", "Prabumulih Timur", "Prabumulih Utara", "Prabumulih Selatan"],
     ["Prabumulih Barat", "Prabumulih Timur", "Prabumulih Utara"],
     [31111, 31114, 31121]),
    ("Pagar Alam", "167301",
     ["Dempo Utara", "Dempo Selatan", "Dempo Tengah", "Pagar Alam Selatan", "Pagar Alam Utara"],
     ["Dempo Utara", "Dempo Selatan", "Pagar Alam Selatan", "Pagar Alam Utara"],
     [31511, 31514, 31519, 31521]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI BENGKULU (17)
# ─────────────────────────────────────────────────────────────────────────────
_BENGKULU = [
    ("Bengkulu", "177101",
     ["Ratu Agung", "Ratu Samban", "Singaran Pati", "Selebar", "Gading Cempaka",
      "Kampung Melayu", "Sungai Serut", "Muara Bangka Hulu", "Teluk Segara"],
     ["Ratu Agung", "Ratu Samban", "Singaran Pati", "Selebar", "Gading Cempaka"],
     [38111, 38116, 38119, 38214, 38122]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI LAMPUNG (18)
# ─────────────────────────────────────────────────────────────────────────────
_LAMPUNG = [
    ("Bandar Lampung", "187101",
     ["Kedaton", "Rajabasa", "Tanjung Karang Barat", "Tanjung Karang Pusat",
      "Tanjung Karang Timur", "Teluk Betung Barat", "Teluk Betung Selatan",
      "Teluk Betung Timur", "Teluk Betung Utara", "Panjang", "Way Halim",
      "Sukarame", "Kemiling", "Langkapura"],
     ["Kedaton", "Rajabasa", "Tanjung Karang Barat", "Tanjung Karang Pusat",
      "Tanjung Karang Timur", "Teluk Betung Barat", "Way Halim", "Sukarame"],
     [35157, 35144, 35128, 35118, 35129, 35223, 35145, 35153]),
    ("Metro", "187201",
     ["Metro Pusat", "Metro Timur", "Metro Barat", "Metro Utara", "Metro Selatan"],
     ["Metro Pusat", "Metro Timur", "Metro Barat", "Metro Utara"],
     [34111, 34124, 34126, 34128]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI DKI JAKARTA (31)
# ─────────────────────────────────────────────────────────────────────────────
_JAKARTA = [
    ("Jakarta Pusat", "317101",
     ["Gambir", "Cideng", "Petojo Utara", "Petojo Selatan", "Kebon Kelapa",
      "Tanah Abang", "Bendungan Hilir", "Senen", "Bungur", "Kemayoran",
      "Menteng", "Gondangdia", "Cikini", "Pegangsaan"],
     ["Gambir", "Tanah Abang", "Senen", "Kemayoran", "Menteng", "Sawah Besar"],
     [10110, 10160, 10410, 10620, 10350, 10740]),
    ("Jakarta Utara", "317201",
     ["Penjaringan", "Pluit", "Penjagalan", "Tanjung Priok", "Kebon Bawang",
      "Sunter Agung", "Sunter Jaya", "Kelapa Gading", "Pegangsaan Dua",
      "Koja", "Lagoa", "Rawa Badak"],
     ["Penjaringan", "Tanjung Priok", "Koja", "Kelapa Gading", "Pademangan"],
     [14440, 14310, 14220, 14240, 14420]),
    ("Jakarta Barat", "317301",
     ["Tamansari", "Pinangsia", "Kebon Jeruk", "Meruya", "Cengkareng",
      "Kapuk", "Penjaringan", "Grogol", "Jelambar", "Kalideres", "Tegal Alur"],
     ["Tamansari", "Kebon Jeruk", "Cengkareng", "Grogol Petamburan", "Kalideres"],
     [11110, 11630, 11730, 11460, 11840]),
    ("Jakarta Selatan", "317401",
     ["Kebayoran Baru", "Cilandak", "Pasar Minggu", "Tebet", "Mampang Prapatan",
      "Pancoran", "Setiabudi", "Pesanggrahan", "Kebayoran Lama", "Jagakarsa"],
     ["Kebayoran Baru", "Cilandak", "Pasar Minggu", "Tebet", "Mampang Prapatan",
      "Pancoran", "Setiabudi"],
     [12110, 12430, 12520, 12810, 12770, 12780, 12920]),
    ("Jakarta Timur", "317501",
     ["Cakung", "Cipayung", "Ciracas", "Duren Sawit", "Jatinegara",
      "Kramat Jati", "Makasar", "Matraman", "Pasar Rebo", "Pulo Gadung"],
     ["Cakung", "Cipayung", "Ciracas", "Duren Sawit", "Jatinegara",
      "Kramat Jati", "Makasar", "Pulo Gadung"],
     [13910, 13840, 13750, 13460, 13310, 13510, 13570, 13210]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI JAWA BARAT (32)
# ─────────────────────────────────────────────────────────────────────────────
_JABAR = [
    ("Bandung", "327301",
     ["Coblong", "Cicendo", "Regol", "Batununggal", "Lengkong", "Cibeunying Kaler",
      "Cibeunying Kidul", "Bandung Wetan", "Bandung Kulon", "Sumur Bandung",
      "Antapani", "Arcamanik", "Astanaanyar", "Babakan Ciparay", "Andir",
      "Bojongloa Kaler", "Bojongloa Kidul", "Buahbatu", "Cibiru", "Cicadas"],
     ["Coblong", "Cicendo", "Regol", "Lengkong", "Cibeunying Kaler",
      "Antapani", "Arcamanik", "Astanaanyar", "Andir", "Bojongloa Kaler",
      "Buahbatu", "Gedebage", "Kiaracondong", "Sumur Bandung"],
     [40132, 40171, 40251, 40264, 40122, 40291, 40292, 40241, 40213, 40232,
      40267, 40294, 40285, 40111]),
    ("Bogor", "327101",
     ["Bogor Utara", "Bogor Selatan", "Bogor Timur", "Bogor Barat", "Bogor Tengah",
      "Tanah Sareal", "Baranangsiang", "Taman Sari", "Empang"],
     ["Bogor Utara", "Bogor Selatan", "Bogor Timur", "Bogor Barat", "Bogor Tengah",
      "Tanah Sareal"],
     [16112, 16133, 16143, 16119, 16121, 16161]),
    ("Depok", "327601",
     ["Pancoran Mas", "Cipayung", "Sukmajaya", "Cimanggis", "Tapos",
      "Sawangan", "Bojongsari", "Beji", "Cinere", "Limo"],
     ["Pancoran Mas", "Cipayung", "Sukmajaya", "Cimanggis", "Tapos",
      "Sawangan", "Bojongsari", "Beji"],
     [16431, 16437, 16412, 16452, 16457, 16511, 16517, 16421]),
    ("Bekasi", "327501",
     ["Bekasi Utara", "Bekasi Selatan", "Bekasi Timur", "Bekasi Barat",
      "Pondok Gede", "Jatiasih", "Mustika Jaya", "Medan Satria",
      "Rawalumbu", "Bantargebang", "Jatisampurna"],
     ["Bekasi Utara", "Bekasi Selatan", "Bekasi Timur", "Bekasi Barat",
      "Pondok Gede", "Jatiasih", "Mustika Jaya", "Medan Satria"],
     [17121, 17148, 17113, 17132, 17413, 17423, 17158, 17131]),
    ("Cimahi", "327401",
     ["Cimahi Utara", "Cimahi Tengah", "Cimahi Selatan"],
     ["Cimahi Utara", "Cimahi Tengah", "Cimahi Selatan"],
     [40512, 40522, 40531]),
    ("Tasikmalaya", "327801",
     ["Tawang", "Cihideung", "Cipedes", "Indihiang", "Kawalu",
      "Mangkubumi", "Purbaratu", "Bungursari"],
     ["Tawang", "Cihideung", "Cipedes", "Indihiang", "Kawalu", "Mangkubumi"],
     [46114, 46122, 46131, 46151, 46182, 46115]),
    ("Cirebon", "327101",
     ["Kejaksan", "Kesambi", "Lemahwungkuk", "Harjamukti", "Pekalipan"],
     ["Kejaksan", "Kesambi", "Lemahwungkuk", "Harjamukti", "Pekalipan"],
     [45121, 45132, 45111, 45143, 45113]),
    ("Sukabumi", "327201",
     ["Baros", "Cibeureum", "Citamiang", "Gunungpuyuh", "Lembursitu",
      "Warudoyong", "Cikole"],
     ["Baros", "Cibeureum", "Citamiang", "Gunungpuyuh", "Warudoyong"],
     [43115, 43121, 43113, 43116, 43132]),
    ("Karawang", "320201",
     ["Karawang Barat", "Karawang Timur", "Adiarsa Barat", "Adiarsa Timur",
      "Tanjungpura", "Nagasari", "Mekarjati"],
     ["Karawang Barat", "Karawang Timur"],
     [41311, 41316]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI BANTEN (36)
# ─────────────────────────────────────────────────────────────────────────────
_BANTEN = [
    ("Tangerang", "367101",
     ["Benda", "Batuceper", "Neglasari", "Periuk", "Cibodas", "Karawaci",
      "Ciledug", "Larangan", "Karangtengah", "Cipondoh", "Pinang", "Tangerang"],
     ["Benda", "Neglasari", "Periuk", "Cibodas", "Karawaci",
      "Ciledug", "Larangan", "Cipondoh", "Pinang", "Tangerang"],
     [15121, 15124, 15132, 15141, 15115, 15151, 15153, 15148, 15155]),
    ("Tangerang Selatan", "367401",
     ["Serpong", "Serpong Utara", "Ciputat", "Ciputat Timur", "Pamulang",
      "Pondok Aren", "Setu"],
     ["Serpong", "Serpong Utara", "Ciputat", "Ciputat Timur", "Pamulang",
      "Pondok Aren", "Setu"],
     [15310, 15325, 15411, 15412, 15416, 15224, 15315]),
    ("Serang", "367301",
     ["Serang", "Cipocok Jaya", "Taktakan", "Kasemen", "Walantaka", "Curug"],
     ["Serang", "Cipocok Jaya", "Taktakan", "Kasemen", "Walantaka"],
     [42111, 42122, 42161, 42182, 42153]),
    ("Cilegon", "367201",
     ["Cilegon", "Ciwandan", "Pulomerak", "Grogol", "Purwakarta", "Citangkil",
      "Jombang", "Cibeber"],
     ["Cilegon", "Ciwandan", "Purwakarta", "Citangkil", "Jombang", "Cibeber"],
     [42411, 42443, 42435, 42422, 42417, 42421]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI JAWA TENGAH (33)
# ─────────────────────────────────────────────────────────────────────────────
_JATENG = [
    ("Semarang", "337401",
     ["Semarang Barat", "Semarang Timur", "Semarang Utara", "Semarang Selatan",
      "Semarang Tengah", "Banyumanik", "Pedurungan", "Candisari", "Gayamsari",
      "Gajah Mungkur", "Genuk", "Gunungpati", "Mijen", "Ngaliyan", "Tembalang"],
     ["Semarang Barat", "Semarang Timur", "Semarang Utara", "Semarang Selatan",
      "Semarang Tengah", "Banyumanik", "Pedurungan", "Candisari", "Gajahmungkur",
      "Genuk", "Gunungpati", "Ngaliyan", "Tembalang"],
     [50141, 50125, 50175, 50252, 50134, 50268, 50197, 50223, 50232, 50112]),
    ("Surakarta", "337201",
     ["Banjarsari", "Serengan", "Pasarkliwon", "Laweyan", "Jebres",
      "Sangkrah", "Gajahan", "Semanggi", "Kadipiro", "Nusukan"],
     ["Banjarsari", "Serengan", "Pasarkliwon", "Laweyan", "Jebres"],
     [57134, 57155, 57111, 57143, 57125]),
    ("Magelang", "337101",
     ["Magelang Utara", "Magelang Tengah", "Magelang Selatan"],
     ["Magelang Utara", "Magelang Tengah", "Magelang Selatan"],
     [56111, 56121, 56124]),
    ("Salatiga", "337301",
     ["Argomulyo", "Sidomukti", "Sidorejo", "Tingkir"],
     ["Argomulyo", "Sidomukti", "Sidorejo", "Tingkir"],
     [50722, 50722, 50714, 50741]),
    ("Pekalongan", "337501",
     ["Pekalongan Barat", "Pekalongan Timur", "Pekalongan Utara", "Pekalongan Selatan"],
     ["Pekalongan Barat", "Pekalongan Timur", "Pekalongan Utara", "Pekalongan Selatan"],
     [51111, 51127, 51148, 51111]),
    ("Tegal", "337601",
     ["Tegal Barat", "Tegal Timur", "Tegal Selatan", "Margadana"],
     ["Tegal Barat", "Tegal Timur", "Tegal Selatan", "Margadana"],
     [52113, 52124, 52131, 52142]),
    ("Cilacap", "330101",
     ["Cilacap Selatan", "Cilacap Tengah", "Cilacap Utara", "Jeruklegi", "Sidareja"],
     ["Cilacap Selatan", "Cilacap Tengah", "Cilacap Utara"],
     [53212, 53221, 53232]),
    ("Purwokerto", "330201",
     ["Purwokerto Barat", "Purwokerto Timur", "Purwokerto Utara", "Purwokerto Selatan"],
     ["Purwokerto Barat", "Purwokerto Timur", "Purwokerto Utara", "Purwokerto Selatan"],
     [53132, 53115, 53127, 53145]),
    ("Kudus", "330901",
     ["Kota", "Gribig", "Jati", "Mejobo", "Gebog"],
     ["Kota", "Jati", "Mejobo"],
     [59311, 59322, 59332]),
    ("Pati", "331101",
     ["Pati", "Gabus", "Wedarijaksa", "Juwana"],
     ["Pati", "Gabus"],
     [59111, 59162]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI DI YOGYAKARTA (34)
# ─────────────────────────────────────────────────────────────────────────────
_DIY = [
    ("Yogyakarta", "347101",
     ["Danurejan", "Gedongtengen", "Gondokusuman", "Gondomanan", "Jetis",
      "Kotagede", "Kraton", "Mantrijeron", "Mergangsan", "Ngampilan",
      "Pakualaman", "Tegalrejo", "Umbulharjo", "Wirobrajan"],
     ["Danurejan", "Gedongtengen", "Gondokusuman", "Gondomanan", "Jetis",
      "Kotagede", "Kraton", "Mantrijeron", "Mergangsan", "Umbulharjo", "Tegalrejo"],
     [55211, 55271, 55221, 55122, 55231, 55171, 55131, 55141, 55153, 55161, 55241]),
    ("Sleman", "340101",
     ["Gamping", "Mlati", "Depok", "Ngemplak", "Ngaglik", "Godean", "Moyudan"],
     ["Gamping", "Mlati", "Depok", "Ngemplak", "Ngaglik"],
     [55291, 55285, 55281, 55584, 55581]),
    ("Bantul", "340201",
     ["Bantul", "Banguntapan", "Kasihan", "Sewon", "Pleret"],
     ["Bantul", "Banguntapan", "Kasihan", "Sewon"],
     [55711, 55198, 55182, 55186]),
    ("Gunung Kidul", "340301",
     ["Wonosari", "Playen", "Patuk", "Gedangsari"],
     ["Wonosari", "Playen"],
     [55811, 55861]),
    ("Kulon Progo", "340401",
     ["Wates", "Pengasih", "Sentolo", "Nanggulan"],
     ["Wates", "Pengasih"],
     [55611, 55652]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI JAWA TIMUR (35)
# ─────────────────────────────────────────────────────────────────────────────
_JATIM = [
    ("Trenggalek", "350301",
     ["Ngetal", "Kelutan", "Sumbergedong", "Ngantru", "Surodakan", "Durenan", "Karangan"],
     ["Pogalan", "Trenggalek", "Durenan", "Karangan", "Gandusari"],
     [66371, 66311, 66312, 66381]),
    ("Tulungagung", "350401",
     ["Bago", "Kepatihan", "Kampungdalem", "Tertek", "Kenayan", "Sembung", "Kutoanyar"],
     ["Tulungagung", "Kedungwaru", "Boyolangu", "Kauman", "Ngunut"],
     [66212, 66213, 66217, 66219]),
    ("Batu", "357901",
     ["Sisir", "Temas", "Songgokerto", "Oro-oro Ombo", "Sidomulyo", "Bumiaji", "Pesanggrahan"],
     ["Batu", "Bumiaji", "Junrejo"],
     [65311, 65314, 65315, 65331]),
    ("Malang", "357301",
     ["Klojen", "Lowokwaru", "Sukun", "Blimbing", "Kedungkandang",
      "Dinoyo", "Tulusrejo", "Kasin", "Kiduldalem", "Kesatrian",
      "Sawojajar", "Ciptomulyo"],
     ["Klojen", "Lowokwaru", "Sukun", "Blimbing", "Kedungkandang"],
     [65111, 65141, 65144, 65126, 65148]),
    ("Surabaya", "357801",
     ["Gubeng", "Wonokromo", "Rungkut", "Tegalsari", "Tambaksari",
      "Sawahan", "Sukolilo", "Semampir", "Kenjeran", "Bubutan",
      "Simokerto", "Genteng", "Krembangan", "Lakarsantri", "Benowo"],
     ["Gubeng", "Wonokromo", "Rungkut", "Tegalsari", "Tambaksari",
      "Semampir", "Kenjeran", "Bubutan", "Genteng", "Krembangan"],
     [60281, 60241, 60293, 60262, 60131, 60151, 60122, 60173, 60271]),
    ("Kediri", "357101",
     ["Mojoroto", "Pesantren", "Kota", "Banjaran", "Ngronggo", "Semampir"],
     ["Mojoroto", "Kota", "Pesantren"],
     [64111, 64121, 64131]),
    ("Blitar", "357201",
     ["Kepanjenkidul", "Sukorejo", "Sananwetan", "Bendo", "Kauman"],
     ["Kepanjenkidul", "Sukorejo", "Sananwetan"],
     [66111, 66121, 66131]),
    ("Sidoarjo", "351501",
     ["Sidokumpul", "Pucang", "Lemahputro", "Magersari", "Celep", "Waru",
      "Taman", "Gedangan", "Sedati", "Porong"],
     ["Sidoarjo", "Waru", "Candi", "Buduran", "Taman", "Gedangan"],
     [61212, 61213, 61256, 61252, 61257]),
    ("Jember", "350901",
     ["Sumbersari", "Patrang", "Kaliwates", "Ajung", "Ambulu"],
     ["Sumbersari", "Patrang", "Kaliwates"],
     [68121, 68118, 68131]),
    ("Jombang", "350701",
     ["Jombang", "Peterongan", "Diwek", "Gudo", "Ploso"],
     ["Jombang", "Peterongan", "Diwek"],
     [61419, 61418, 61471]),
    ("Mojokerto", "357601",
     ["Prajurit Kulon", "Magersari"],
     ["Prajurit Kulon", "Magersari"],
     [61321, 61311]),
    ("Madiun", "357401",
     ["Taman", "Mangunharjo", "Kartoharjo"],
     ["Taman", "Mangunharjo", "Kartoharjo"],
     [63121, 63131, 63137]),
    ("Gresik", "350301",
     ["Gresik", "Kebomas", "Manyar", "Duduksampeyan"],
     ["Gresik", "Kebomas", "Manyar"],
     [61111, 61122, 61151]),
    ("Lamongan", "350701",
     ["Lamongan", "Turi", "Tikung", "Babat"],
     ["Lamongan", "Turi"],
     [62212, 62218]),
    ("Banyuwangi", "351001",
     ["Banyuwangi", "Kalipuro", "Giri", "Glagah", "Kabat"],
     ["Banyuwangi", "Kalipuro", "Giri"],
     [68411, 68421, 68416]),
    ("Probolinggo", "357701",
     ["Kademangan", "Mayangan", "Wonoasih", "Kanigaran", "Kedopok"],
     ["Kademangan", "Mayangan", "Wonoasih", "Kanigaran"],
     [67212, 67218, 67214, 67213]),
    ("Pasuruan", "357501",
     ["Bugul Kidul", "Gadingrejo", "Purworejo", "Pohjentrek"],
     ["Bugul Kidul", "Gadingrejo", "Purworejo"],
     [67112, 67114, 67116]),
    ("Lumajang", "350803",
     ["Lumajang", "Tekung", "Yosowilangun", "Randuagung"],
     ["Lumajang", "Tekung"],
     [67317, 67318]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI BALI (51)
# ─────────────────────────────────────────────────────────────────────────────
_BALI = [
    ("Denpasar", "517101",
     ["Denpasar Barat", "Denpasar Timur", "Denpasar Utara", "Denpasar Selatan",
      "Padangsambian", "Pemecutan", "Tonja", "Peguyangan", "Dangin Puri"],
     ["Denpasar Barat", "Denpasar Timur", "Denpasar Utara", "Denpasar Selatan"],
     [80117, 80232, 80116, 80224]),
    ("Badung", "510201",
     ["Mengwi", "Abiansemal", "Kuta", "Kuta Selatan", "Kuta Utara", "Petang"],
     ["Mengwi", "Kuta", "Kuta Selatan", "Kuta Utara", "Abiansemal"],
     [80351, 80361, 80361, 80362, 80352]),
    ("Gianyar", "510301",
     ["Gianyar", "Blahbatuh", "Sukawati", "Payangan", "Tampaksiring"],
     ["Gianyar", "Blahbatuh", "Sukawati"],
     [80511, 80581, 80582]),
    ("Tabanan", "510401",
     ["Tabanan", "Kerambitan", "Kediri", "Marga", "Selemadeg"],
     ["Tabanan", "Kerambitan", "Kediri"],
     [82111, 82151, 82121]),
    ("Buleleng", "510801",
     ["Buleleng", "Sukasada", "Seririt", "Banjar"],
     ["Buleleng", "Sukasada"],
     [81111, 81119]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI NUSA TENGGARA BARAT (52)
# ─────────────────────────────────────────────────────────────────────────────
_NTB = [
    ("Mataram", "527101",
     ["Ampenan", "Cakranegara", "Mataram", "Sandubaya", "Sekarbela", "Selaparang"],
     ["Ampenan", "Cakranegara", "Mataram", "Sandubaya", "Sekarbela", "Selaparang"],
     [83114, 83239, 83121, 83125, 83116, 83122]),
    ("Bima", "527201",
     ["Rasanae Barat", "Rasanae Timur", "Asakota", "Raba", "Mpunda"],
     ["Rasanae Barat", "Rasanae Timur", "Asakota", "Raba", "Mpunda"],
     [84113, 84119, 84139, 84133, 84118]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI NUSA TENGGARA TIMUR (53)
# ─────────────────────────────────────────────────────────────────────────────
_NTT = [
    ("Kupang", "537101",
     ["Oebobo", "Kota Raja", "Kota Lama", "Alak", "Kelapa Lima", "Maulafa"],
     ["Oebobo", "Kota Raja", "Kota Lama", "Alak", "Kelapa Lima"],
     [85111, 85116, 85228, 85113, 85117]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI KALIMANTAN BARAT (61)
# ─────────────────────────────────────────────────────────────────────────────
_KALBAR = [
    ("Pontianak", "617101",
     ["Pontianak Kota", "Pontianak Barat", "Pontianak Selatan", "Pontianak Timur",
      "Pontianak Utara", "Pontianak Tenggara"],
     ["Pontianak Kota", "Pontianak Barat", "Pontianak Selatan", "Pontianak Timur",
      "Pontianak Utara"],
     [78111, 78121, 78122, 78112, 78241]),
    ("Singkawang", "617201",
     ["Singkawang Barat", "Singkawang Tengah", "Singkawang Timur",
      "Singkawang Utara", "Singkawang Selatan"],
     ["Singkawang Barat", "Singkawang Tengah", "Singkawang Timur", "Singkawang Utara"],
     [79112, 79116, 79151, 79122]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI KALIMANTAN TENGAH (62)
# ─────────────────────────────────────────────────────────────────────────────
_KALTENG = [
    ("Palangkaraya", "627101",
     ["Pahandut", "Jekan Raya", "Bukit Tunggal", "Rakumpit", "Sabangau"],
     ["Pahandut", "Jekan Raya", "Bukit Tunggal", "Sabangau"],
     [73111, 73112, 73113, 73116]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI KALIMANTAN SELATAN (63)
# ─────────────────────────────────────────────────────────────────────────────
_KALSEL = [
    ("Banjarmasin", "637101",
     ["Banjarmasin Barat", "Banjarmasin Timur", "Banjarmasin Tengah",
      "Banjarmasin Utara", "Banjarmasin Selatan",
      "Sungai Mesa", "Teluk Dalam", "Melayu"],
     ["Banjarmasin Barat", "Banjarmasin Timur", "Banjarmasin Tengah",
      "Banjarmasin Utara", "Banjarmasin Selatan"],
     [70111, 70236, 70111, 70125, 70243]),
    ("Banjarbaru", "637201",
     ["Landasan Ulin", "Liang Anggang", "Cempaka", "Banjarbaru Utara", "Banjarbaru Selatan"],
     ["Landasan Ulin", "Liang Anggang", "Cempaka", "Banjarbaru Utara", "Banjarbaru Selatan"],
     [70712, 70724, 70711, 70722, 70721]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI KALIMANTAN TIMUR (64)
# ─────────────────────────────────────────────────────────────────────────────
_KALTIM = [
    ("Samarinda", "647201",
     ["Samarinda Ulu", "Samarinda Ilir", "Samarinda Kota", "Loa Janan Ilir",
      "Palaran", "Sungai Kunjang", "Sambutan", "Samarinda Seberang",
      "Samarinda Utara"],
     ["Samarinda Ulu", "Samarinda Ilir", "Samarinda Kota", "Loa Janan Ilir",
      "Palaran", "Sungai Kunjang", "Samarinda Seberang"],
     [75122, 75133, 75111, 75242, 75251, 75126, 75131]),
    ("Balikpapan", "647201",
     ["Balikpapan Barat", "Balikpapan Kota", "Balikpapan Selatan",
      "Balikpapan Timur", "Balikpapan Utara", "Balikpapan Tengah"],
     ["Balikpapan Barat", "Balikpapan Kota", "Balikpapan Selatan",
      "Balikpapan Timur", "Balikpapan Utara"],
     [76131, 76111, 76115, 76116, 76125, 76123]),
    ("Bontang", "647301",
     ["Bontang Barat", "Bontang Selatan", "Bontang Utara"],
     ["Bontang Barat", "Bontang Selatan", "Bontang Utara"],
     [75311, 75315, 75313]),
    ("Kutai Kartanegara", "640201",
     ["Tenggarong", "Loa Janan", "Muara Badak", "Sangasanga"],
     ["Tenggarong", "Loa Janan"],
     [75511, 75531]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SULAWESI UTARA (71)
# ─────────────────────────────────────────────────────────────────────────────
_SULUT = [
    ("Manado", "717101",
     ["Wenang", "Sario", "Tikala", "Mapanget", "Malalayang", "Tuminting",
      "Bunaken", "Wanea", "Paal Dua", "Singkil"],
     ["Wenang", "Sario", "Tikala", "Mapanget", "Malalayang", "Tuminting", "Wanea"],
     [95111, 95116, 95127, 95124, 95119, 95113, 95125]),
    ("Bitung", "717201",
     ["Aertembaga", "Girian", "Lembeh Selatan", "Lembeh Utara", "Madidir",
      "Maesa", "Matuari", "Ranowulu"],
     ["Aertembaga", "Girian", "Madidir", "Maesa", "Ranowulu"],
     [95521, 95511, 95514, 95512, 95522]),
    ("Tomohon", "717301",
     ["Tomohon Barat", "Tomohon Tengah", "Tomohon Timur", "Tomohon Utara", "Tomohon Selatan"],
     ["Tomohon Barat", "Tomohon Tengah", "Tomohon Timur", "Tomohon Utara"],
     [95361, 95362, 95371, 95381]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SULAWESI TENGAH (72)
# ─────────────────────────────────────────────────────────────────────────────
_SULTENG = [
    ("Palu", "727101",
     ["Palu Barat", "Palu Timur", "Palu Selatan", "Palu Utara", "Tatanga",
      "Ulujadi", "Mantikulore", "Tawaeli"],
     ["Palu Barat", "Palu Timur", "Palu Selatan", "Palu Utara", "Tatanga"],
     [94111, 94118, 94112, 94124, 94115]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SULAWESI SELATAN (73)
# ─────────────────────────────────────────────────────────────────────────────
_SULSEL = [
    ("Makassar", "737101",
     ["Ujung Pandang", "Makassar", "Rappocini", "Panakkukang", "Manggala",
      "Tamalanrea", "Biringkanaya", "Tamalate", "Mamajang", "Bontoala",
      "Wajo", "Mariso", "Ujung Tanah", "Kepulauan Sangkarrang",
      "Tallo", "Somba Opu"],
     ["Ujung Pandang", "Makassar", "Rappocini", "Panakkukang", "Manggala",
      "Tamalanrea", "Biringkanaya", "Tamalate", "Mamajang", "Bontoala",
      "Wajo", "Mariso", "Tallo"],
     [90111, 90125, 90222, 90231, 90234, 90245, 90241, 90212, 90134, 90151,
      90112, 90123, 90152]),
    ("Parepare", "737201",
     ["Bacukiki", "Bacukiki Barat", "Ujung", "Soreang"],
     ["Bacukiki", "Bacukiki Barat", "Ujung", "Soreang"],
     [91112, 91121, 91112, 91122]),
    ("Palopo", "737301",
     ["Wara", "Wara Selatan", "Wara Utara", "Wara Timur", "Wara Barat",
      "Sendana", "Bara", "Telluwanua", "Mungkajang"],
     ["Wara", "Wara Selatan", "Wara Utara", "Wara Timur", "Wara Barat",
      "Sendana", "Bara"],
     [91911, 91921, 91912, 91913, 91914, 91915, 91916]),
    ("Gowa", "730601",
     ["Somba Opu", "Bontomarannu", "Palangga", "Barombong", "Bajeng"],
     ["Somba Opu", "Bontomarannu", "Palangga"],
     [92114, 92116, 92115]),
    ("Bone", "730601",
     ["Tanete Riattang", "Tanete Riattang Barat", "Tanete Riattang Timur"],
     ["Tanete Riattang", "Tanete Riattang Barat"],
     [92711, 92713]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SULAWESI TENGGARA (74)
# ─────────────────────────────────────────────────────────────────────────────
_SULTRA = [
    ("Kendari", "747101",
     ["Abeli", "Baruga", "Kadia", "Kambu", "Kendari", "Kendari Barat",
      "Mandonga", "Poasia", "Puuwatu", "Wua-wua"],
     ["Abeli", "Baruga", "Kadia", "Kambu", "Kendari", "Kendari Barat",
      "Mandonga", "Poasia"],
     [93111, 93118, 93116, 93112, 93117, 93114, 93113, 93115]),
    ("Bau-Bau", "747201",
     ["Batupoaro", "Betoambari", "Bungi", "Kokalukuna", "Lea-Lea",
      "Murhum", "Sorawolio", "Waborobo", "Wolio"],
     ["Batupoaro", "Betoambari", "Bungi", "Kokalukuna", "Murhum", "Wolio"],
     [93711, 93725, 93731, 93712, 93721, 93714]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI GORONTALO (75)
# ─────────────────────────────────────────────────────────────────────────────
_GORONTALO = [
    ("Gorontalo", "757101",
     ["Dungingi", "Dumbo Raya", "Hulonthalangi", "Kota Barat", "Kota Selatan",
      "Kota Tengah", "Kota Timur", "Kota Utara", "Sipatana", "Wongkaditi"],
     ["Dungingi", "Dumbo Raya", "Kota Barat", "Kota Selatan",
      "Kota Tengah", "Kota Timur", "Kota Utara", "Sipatana"],
     [96115, 96111, 96112, 96117, 96118, 96119, 96125, 96113]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI SULAWESI BARAT (76)
# ─────────────────────────────────────────────────────────────────────────────
_SULBAR = [
    ("Mamuju", "760101",
     ["Binanga", "Beru-Beru", "Karema", "Mamuju", "Rimuku"],
     ["Binanga", "Karema", "Mamuju", "Rimuku"],
     [91512, 91511, 91514, 91512]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI MALUKU (81)
# ─────────────────────────────────────────────────────────────────────────────
_MALUKU = [
    ("Ambon", "817101",
     ["Nusaniwe", "Sirimau", "Teluk Ambon", "Teluk Ambon Baguala", "Leitimur Selatan",
      "Batu Gajah", "Karang Panjang", "Waihaong"],
     ["Nusaniwe", "Sirimau", "Teluk Ambon", "Teluk Ambon Baguala"],
     [97115, 97128, 97231, 97232]),
    ("Tual", "817201",
     ["Dullah Utara", "Dullah Selatan", "Kur Selatan", "Pulau-Pulau Kei Kecil",
      "Pulau-Pulau Kei Kecil Barat", "Tayando Tam"],
     ["Dullah Utara", "Dullah Selatan", "Pulau-Pulau Kei Kecil"],
     [97611, 97612, 97613]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI PAPUA BARAT (92)
# ─────────────────────────────────────────────────────────────────────────────
_PAPUA_BARAT = [
    ("Sorong", "927101",
     ["Sorong", "Sorong Barat", "Sorong Timur", "Sorong Utara",
      "Sorong Manoi", "Klaligi", "Malaingkedi", "Malawele"],
     ["Sorong", "Sorong Barat", "Sorong Timur", "Sorong Utara"],
     [98411, 98414, 98416, 98418]),
    ("Manokwari", "920101",
     ["Manokwari Barat", "Manokwari Selatan", "Manokwari Timur", "Manokwari Utara",
      "Warmare", "Prafi", "Tanah Rubu"],
     ["Manokwari Barat", "Manokwari Selatan", "Manokwari Timur", "Manokwari Utara"],
     [98312, 98315, 98313, 98311]),
]

# ─────────────────────────────────────────────────────────────────────────────
# PROVINSI PAPUA (94)
# ─────────────────────────────────────────────────────────────────────────────
_PAPUA = [
    ("Jayapura", "947101",
     ["Abepura", "Heram", "Jayapura Selatan", "Jayapura Utara", "Muara Tami"],
     ["Abepura", "Heram", "Jayapura Selatan", "Jayapura Utara"],
     [99111, 99118, 99112, 99114]),
]

# ─────────────────────────────────────────────────────────────────────────────
# GABUNGAN SEMUA DATA KOTA / WILAYAH
# ─────────────────────────────────────────────────────────────────────────────
KOTA_WILAYAH = (
    _ACEH
    + _SUMUT
    + _SUMBAR
    + _RIAU
    + _KEPRI
    + _JAMBI
    + _SUMSEL
    + _BENGKULU
    + _LAMPUNG
    + _JAKARTA
    + _JABAR
    + _BANTEN
    + _JATENG
    + _DIY
    + _JATIM
    + _BALI
    + _NTB
    + _NTT
    + _KALBAR
    + _KALTENG
    + _KALSEL
    + _KALTIM
    + _SULUT
    + _SULTENG
    + _SULSEL
    + _SULTRA
    + _GORONTALO
    + _SULBAR
    + _MALUKU
    + _PAPUA_BARAT
    + _PAPUA
)

# ─────────────────────────────────────────────────────────────────────────────
# NAMA JALAN
# ─────────────────────────────────────────────────────────────────────────────
STREET_NAMES = [
    # Nama pahlawan & tokoh nasional
    "Diponegoro", "Sudirman", "Gajah Mada", "Pahlawan", "Merdeka",
    "Imam Bonjol", "Ahmad Yani", "Kartini", "Hayam Wuruk", "Veteran",
    "Sisingamangaraja", "Teuku Umar", "Cut Nyak Dien", "Patimura",
    "Hasanuddin", "Tuanku Tambusai", "Sultan Agung", "Pangeran Antasari",
    "Pangeran Diponegoro", "Kapten Tendean", "Jenderal Sudirman",
    "Abdul Muis", "Letjen Suprapto", "Brigjen Katamso",
    # Nama bunga & alam
    "Melati", "Mawar", "Kenanga", "Dahlia", "Flamboyan",
    "Anggrek", "Cempaka", "Kamboja", "Tulip", "Bougenville",
    "Teratai", "Nusa Indah", "Bougainville", "Seruni",
    # Nama umum
    "Raya", "Utama", "Indah", "Bahagia", "Sejahtera", "Harmoni",
    "Veteran", "Perjuangan", "Kebon Jeruk", "Mangga Besar",
    "Haji Agus Salim", "Proklamasi", "Nasional", "Reformasi",
    "Pemuda", "Persatuan", "Kesatuan", "Keadilan", "Kemakmuran",
    # Nama khas daerah
    "Pajajaran", "Siliwangi", "Brawijaya", "Majapahit", "Sriwijaya",
    "Mataram", "Demak", "Singosari", "Kahuripan", "Taruma",
    "Cendrawasih", "Komodo", "Rinjani", "Semeru", "Bromo",
    "Tambora", "Gede", "Merapi", "Merbabu", "Sindoro",
    # Nama lainnya
    "Wolter Monginsidi", "Pierre Tendean", "Zainul Arifin",
    "Sam Ratulangi", "Ratulangi", "Pakis", "Kenari", "Beringin",
    "Akasia", "Jati", "Pinus", "Cemara", "Bambu", "Rambutan",
    "Manggis", "Mangga", "Jeruk", "Pisang", "Pepaya",
]

# ─────────────────────────────────────────────────────────────────────────────
# NAMA DUSUN / KAMPUNG
# ─────────────────────────────────────────────────────────────────────────────
DUSUN_NAMES = [
    "Krajan", "Kebon", "Duwet", "Kedung", "Sumber", "Tengah", "Santren", "Kunden",
    "Bendo", "Jaten", "Ploso", "Manggis", "Ngoto", "Gatak", "Tulung",
    "Ngrejo", "Jangkung", "Kaliputih", "Ngrejek", "Tegalombo",
    "Wonorejo", "Watuagung", "Sumberagung", "Kalianyar", "Sukamaju",
    "Sumberbaru", "Cikaret", "Ciawi", "Babakan", "Leuwiliang",
    "Cibeureum", "Sindangbarang", "Lebak", "Cisarua", "Cipanas",
    "Muara", "Rantau", "Simpang", "Pasar Baru", "Hilir",
    "Hulu", "Pulau", "Sungai", "Batu", "Gunung",
    "Talang", "Parit", "Kampung Baru", "Kampung Atas", "Kampung Bawah",
]

# ─────────────────────────────────────────────────────────────────────────────
# FUNGSI UTAMA
# ─────────────────────────────────────────────────────────────────────────────

def get_random_location() -> dict:
    """
    Menghasilkan data wilayah lengkap secara acak dari seluruh Indonesia.
    """
    kota_info = random.choice(KOTA_WILAYAH)
    kota_nama, wilayah_code, kelurahan_list, kecamatan_list, kodepos_list = kota_info
    return {
        "tempat_lahir": kota_nama,
        "wilayah_code": wilayah_code,
        "kelurahan": random.choice(kelurahan_list),
        "kecamatan": random.choice(kecamatan_list),
        "kode_pos": random.choice(kodepos_list),
        "dusun": (
            "-" if random.random() < 0.55
            else f"Dusun {random.choice(DUSUN_NAMES)}"
        ),
        "alamat": (
            f"Jl. {random.choice(STREET_NAMES)} No. {random.randint(1, 150)}"
            if random.random() < 0.75
            else f"Gang {random.choice(DUSUN_NAMES)} No. {random.randint(1, 30)}"
        ),
        "rt": random.randint(1, 25),
        "rw": random.randint(1, 15),
    }
