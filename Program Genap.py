while True:
    angka = input("Masukkan angka (ketik 'stop' untuk berhenti): ")

    if angka.lower() == "stop":
        print("Program selesai")
        break

    if angka.isdigit():
        angka = int(angka)

        if angka % 2 == 0:
            print(angka, "adalah bilangan GENAP")
        else:
            print(angka, "adalah bilangan GANJIL")
    else:
        print("Input harus berupa angka!")