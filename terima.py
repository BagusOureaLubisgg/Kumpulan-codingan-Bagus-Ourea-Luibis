daftar_nama = ["Bagus", "Pa", "Mi", "Bening", "Fiqo"]

while True:
    nama = input("Ketik Nama Anda = ")

    if nama in daftar_nama:
        print("Selamat Datang")

        pilihan = input("Mau lanjut lagi? (ya/tidak) = ").lower()
        if pilihan == "tidak":
            print("Program berhenti.")
            break
    else:
        print("Akses Ditolak, coba lagi!")
        
        
        
username = str(input("ketik username = "))
password = str(input("ketik password = "))
print()
if username == "CyberGanz" and password == "Kakikanan_45":
    print("login berhasil")
else:
    print("login gagal")