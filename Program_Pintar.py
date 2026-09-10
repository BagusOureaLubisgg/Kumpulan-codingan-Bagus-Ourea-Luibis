import math

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    print("3. Kalkulator Matematika")
    print("4. Kalkulator Trigonometri")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    # ======================
    # BANGUN DATAR
    # ======================
    if pilihan == "1":
        print("\n-- Bangun Datar --")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar Genjang")
        print("6. Trapesium")

        pilih = input("Pilih: ")

        if pilih == "1":
            s = float(input("Sisi: "))
            print("Luas:", s * s)
            print("Keliling:", 4 * s)

        elif pilih == "2":
            p = float(input("Panjang: "))
            l = float(input("Lebar: "))
            print("Luas:", p * l)
            print("Keliling:", 2 * (p + l))

        elif pilih == "3":
            a = float(input("Alas: "))
            t = float(input("Tinggi: "))
            s1 = float(input("Sisi 1: "))
            s2 = float(input("Sisi 2: "))
            s3 = float(input("Sisi 3: "))
            print("Luas:", 0.5 * a * t)
            print("Keliling:", s1 + s2 + s3)

        elif pilih == "4":
            r = float(input("Jari-jari: "))
            print("Luas:", math.pi * r * r)
            print("Keliling:", 2 * math.pi * r)

        elif pilih == "5":
            a = float(input("Alas: "))
            t = float(input("Tinggi: "))
            s = float(input("Sisi miring: "))
            print("Luas:", a * t)
            print("Keliling:", 2 * (a + s))

        elif pilih == "6":
            a = float(input("Sisi atas: "))
            b = float(input("Sisi bawah: "))
            t = float(input("Tinggi: "))
            s1 = float(input("Sisi miring 1: "))
            s2 = float(input("Sisi miring 2: "))
            print("Luas:", 0.5 * (a + b) * t)
            print("Keliling:", a + b + s1 + s2)

    # ======================
    # BANGUN RUANG
    # ======================
    elif pilihan == "2":
        print("\n-- Bangun Ruang --")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Bola")

        pilih = input("Pilih: ")

        if pilih == "1":
            s = float(input("Sisi: "))
            print("Volume:", s**3)
            print("Luas Permukaan:", 6 * s * s)

        elif pilih == "2":
            p = float(input("Panjang: "))
            l = float(input("Lebar: "))
            t = float(input("Tinggi: "))
            print("Volume:", p * l * t)
            print("Luas Permukaan:", 2 * (p*l + p*t + l*t))

        elif pilih == "3":
            r = float(input("Jari-jari: "))
            t = float(input("Tinggi: "))
            print("Volume:", math.pi * r**2 * t)
            print("Luas Permukaan:", 2 * math.pi * r * (r + t))

        elif pilih == "4":
            r = float(input("Jari-jari: "))
            t = float(input("Tinggi: "))
            s = math.sqrt(r**2 + t**2)
            print("Volume:", (1/3) * math.pi * r**2 * t)
            print("Luas Permukaan:", math.pi * r * (r + s))

        elif pilih == "5":
            r = float(input("Jari-jari: "))
            print("Volume:", (4/3) * math.pi * r**3)
            print("Luas Permukaan:", 4 * math.pi * r**2)

    # ======================
    # KALKULATOR MATEMATIKA
    # ======================
    elif pilihan == "3":
        print("\n-- Kalkulator Matematika --")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Pangkat")

        pilih = input("Pilih: ")

        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))

        if pilih == "1":
            print("Hasil:", a + b)
        elif pilih == "2":
            print("Hasil:", a - b)
        elif pilih == "3":
            print("Hasil:", a * b)
        elif pilih == "4":
            if b != 0:
                print("Hasil:", a / b)
            else:
                print("Tidak bisa dibagi 0!")
        elif pilih == "5":
            print("Hasil:", a ** b)

    # ======================
    # KALKULATOR TRIGONOMETRI
    # ======================
    elif pilihan == "4":
        print("\n-- Kalkulator Trigonometri --")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")

        pilih = input("Pilih: ")
        sudut = float(input("Masukkan sudut (derajat): "))

        # konversi ke radian
        rad = math.radians(sudut)

        if pilih == "1":
            print("sin =", math.sin(rad))
        elif pilih == "2":
            print("cos =", math.cos(rad))
        elif pilih == "3":
            print("tan =", math.tan(rad))

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")