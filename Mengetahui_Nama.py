from datetime import datetime

# List untuk menyimpan data
data_orang = []

while True:
    print("\n=== Input Data ===")
    nama = input("Masukkan nama: ")
    tanggal = int(input("Tanggal lahir (1-31): "))
    bulan = int(input("Bulan lahir (1-12): "))
    tahun = int(input("Tahun lahir (contoh: 2005): "))

    # Ambil tanggal sekarang
    sekarang = datetime.now()

    # Hitung umur
    umur = sekarang.year - tahun
    if (sekarang.month, sekarang.day) < (bulan, tanggal):
        umur -= 1

    # Simpan ke dalam list (dictionary)
    data_orang.append({
        "nama": nama,
        "umur": umur
    })

    print(f"Umur {nama} adalah {umur} tahun")

    # Tanya lanjut atau tidak
    lagi = input("Tambah data lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

# Tampilkan semua data
print("\n=== Data Tersimpan ===")
for orang in data_orang:
    print(f"Nama: {orang['nama']}, Umur: {orang['umur']} tahun")