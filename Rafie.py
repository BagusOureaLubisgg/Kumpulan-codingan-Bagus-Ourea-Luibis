import re
import json
import bcrypt
import time
from getpass import getpass
import os
from datetime import datetime

DATA_FILE = "users_secure.json"

# ================= UTIL =================
def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hitung_umur(tahun, bulan, tanggal):
    today = datetime.today()
    umur = today.year - tahun
    if (today.month, today.day) < (bulan, tanggal):
        umur -= 1
    return umur

# ================= VALIDASI =================
def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email)

def valid_password(password):
    return (
        len(password) >= 8 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password)
    )

# ================= REGISTER =================
def register(users):
    print("\n===== REGISTER =====")

    # EMAIL
    while True:
        email = input("Email = ").strip().lower()
        if not valid_email(email):
            print("❌ Email tidak valid!")
        elif email in users:
            print("❌ Email sudah terdaftar!")
        else:
            break

    # PASSWORD
    while True:
        password = getpass("Password (min 8, huruf besar, kecil, angka) = ")
        if not valid_password(password):
            print("❌ Password lemah!")
        else:
            break

    # DATA DIRI
    nama = input("Nama lengkap = ").strip()
    tempat = input("Tempat lahir = ").strip()

    while True:
        try:
            tanggal = int(input("Tanggal lahir (1-31) = "))
            bulan = int(input("Bulan lahir (1-12) = "))
            tahun = int(input("Tahun lahir (contoh: 2005) = "))

            # validasi tanggal real
            datetime(tahun, bulan, tanggal)
            break
        except:
            print("❌ Tanggal tidak valid!")

    umur = hitung_umur(tahun, bulan, tanggal)

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    users[email] = {
        "password": hashed,
        "failed": 0,
        "locked_until": 0,
        "profile": {
            "nama": nama,
            "tempat_lahir": tempat,
            "tanggal_lahir": tanggal,
            "bulan_lahir": bulan,
            "tahun_lahir": tahun,
            "umur": umur
        }
    }

    save_users(users)
    print("✅ Registrasi berhasil!")

# ================= LOGIN =================
def login(users):
    print("\n===== LOGIN =====")

    email = input("Email = ").strip().lower()
    user = users.get(email)

    if not user:
        print("❌ Email atau password salah!")
        return

    if time.time() < user["locked_until"]:
        print("⛔ Akun dikunci sementara!")
        return

    password = getpass("Password = ")

    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        print("🎉 Login berhasil!")

        profile = user["profile"]
        print("\n===== DATA ANDA =====")
        print("Nama:", profile["nama"])
        print("Tempat Lahir:", profile["tempat_lahir"])
        print("Tanggal Lahir:",
              profile["tanggal_lahir"], "-",
              profile["bulan_lahir"], "-",
              profile["tahun_lahir"])
        print("Umur:", profile["umur"], "tahun")

        user["failed"] = 0
    else:
        user["failed"] += 1
        print("❌ Email atau password salah!")

        if user["failed"] >= 3:
            user["locked_until"] = time.time() + 30
            print("⛔ Akun dikunci 30 detik!")

    save_users(users)
    time.sleep(1)

# ================= MAIN =================
def main():
    users = load_users()

    while True:
        print("\n===== MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        pilih = input("Pilih = ")

        if pilih == "1":
            register(users)
        elif pilih == "2":
            login(users)
        elif pilih == "3":
            print("Keluar...")
            break
        else:
            print("❌ Tidak valid!")

if __name__ == "__main__":
    main()