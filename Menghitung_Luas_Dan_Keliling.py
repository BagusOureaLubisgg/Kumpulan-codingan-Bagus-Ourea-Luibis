import math

while True:
    print("\n=== MENU ===")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    # ======================
    # BANGUN DATAR
    # ======================
    if pilihan == "1":
        print("\n-- Bangun Datar --")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")

        pilih = input("Pilih: ")

        if pilih == "1":
            s = float(input("Masukkan sisi: "))
            luas = s * s
            keliling = 4 * s
            print("Luas:", luas)
            print("Keliling:", keliling)

        elif pilih == "2":
            p = float(input("Panjang: "))
            l = float(input("Lebar: "))
            luas = p * l
            keliling = 2 * (p + l)
            print("Luas:", luas)
            print("Keliling:", keliling)

        elif pilih == "3":
            r = float(input("Jari-jari: "))
            luas = math.pi * r * r
            keliling = 2 * math.pi * r
            print("Luas:", luas)
            print("Keliling:", keliling)

    # ======================
    # BANGUN RUANG
    # ======================
    elif pilihan == "2":
        print("\n-- Bangun Ruang --")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")

        pilih = input("Pilih: ")

        if pilih == "1":
            s = float(input("Sisi: "))
            volume = s ** 3
            luas = 6 * s * s
            print("Volume:", volume)
            print("Luas Permukaan:", luas)

        elif pilih == "2":
            p = float(input("Panjang: "))
            l = float(input("Lebar: "))
            t = float(input("Tinggi: "))
            volume = p * l * t
            luas = 2 * (p*l + p*t + l*t)
            print("Volume:", volume)
            print("Luas Permukaan:", luas)

        elif pilih == "3":
            r = float(input("Jari-jari: "))
            t = float(input("Tinggi: "))
            volume = math.pi * r * r * t
            luas = 2 * math.pi * r * (r + t)
            print("Volume:", volume)
            print("Luas Permukaan:", luas)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")