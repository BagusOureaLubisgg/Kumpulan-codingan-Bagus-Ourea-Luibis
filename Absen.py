import json
from datetime import datetime

FILE_NAME = "absen.json"

# Load data dari file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Simpan data ke file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Tambah absen
def tambah_absen():
    data = load_data()

    nama = input("Masukkan nama siswa: ")
    status = input("Status (hadir/tidak): ").lower()

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.append({
        "nama": nama,
        "status": status,
        "tanggal": tanggal
    })

    save_data(data)
    print("Data absen berhasil disimpan!")

# Lihat data absen
def lihat_absen():
    data = load_data()

    if not data:
        print("Belum ada data absen.")
        return

    print("\n=== Data Absen ===")
    for i, d in enumerate(data, 1):
        print(f"{i}. {d['nama']} - {d['status']} ({d['tanggal']})")

# Menu utama
while True:
    print("\n=== MENU ABSEN KELAS ===")
    print("1. Tambah Absen")
    print("2. Lihat Absen")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_absen()
    elif pilihan == "2":
        lihat_absen()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")