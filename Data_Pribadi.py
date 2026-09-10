data_kelas = {
    "nama_kelas": "X RPL 1",
    "wali_kelas": "Pak Andi",
    "jumlah_siswa": 5,
    "siswa": [
        {
            "nis": "001",
            "nama": "Budi",
            "jenis_kelamin": "L",
            "umur": 16
        },
        {
            "nis": "002",
            "nama": "Siti",
            "jenis_kelamin": "P",
            "umur": 16
        },
        {
            "nis": "003",
            "nama": "Andi",
            "jenis_kelamin": "L",
            "umur": 17
        },
        {
            "nis": "004",
            "nama": "Rina",
            "jenis_kelamin": "P",
            "umur": 16
        },
        {
            "nis": "005",
            "nama": "Dewi",
            "jenis_kelamin": "P",
            "umur": 17
        }
    ]
}

# Menampilkan data
print("Nama Kelas:", data_kelas["nama_kelas"])
print("Wali Kelas:", data_kelas["wali_kelas"])
print("Jumlah Siswa:", data_kelas["jumlah_siswa"])

print("\n=== Daftar Siswa ===")
for siswa in data_kelas["siswa"]:
    print(f"{siswa['nis']} - {siswa['nama']} ({siswa['jenis_kelamin']}, {siswa['umur']} tahun)")