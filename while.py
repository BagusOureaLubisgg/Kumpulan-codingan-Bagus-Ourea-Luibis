# List kosong
data = []

while True:
    print("\n=== MENU ===")
    print("1. Tampilkan List")
    print("2. Tambah (Append)")
    print("3. Insert (Tambah di posisi tertentu)")
    print("4. Hapus (Remove)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("Isi list:", data)

    elif pilihan == "2":
        item = input("Masukkan data yang ingin ditambahkan: ")
        data.append(item)
        print("Data berhasil ditambahkan.")

    elif pilihan == "3":
        item = input("Masukkan data: ")
        posisi = int(input("Masukkan posisi index: "))
        data.insert(posisi, item)
        print("Data berhasil di-insert.")

    elif pilihan == "4":
        item = input("Masukkan data yang ingin dihapus: ")
        if item in data:
            data.remove(item)
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan di list.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi!")