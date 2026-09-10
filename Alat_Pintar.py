import tkinter as tk
from tkinter import messagebox
import math

# ======================
# FUNGSI BANGUN DATAR
# ======================
def hitung_persegi():
    try:
        s = float(entry1.get())
        luas = s * s
        keliling = 4 * s
        hasil.set(f"Luas = {luas}, Keliling = {keliling}")
    except:
        messagebox.showerror("Error", "Input tidak valid")

def hitung_persegi_panjang():
    try:
        p = float(entry1.get())
        l = float(entry2.get())
        luas = p * l
        keliling = 2 * (p + l)
        hasil.set(f"Luas = {luas}, Keliling = {keliling}")
    except:
        messagebox.showerror("Error", "Input tidak valid")

def hitung_lingkaran():
    try:
        r = float(entry1.get())
        luas = math.pi * r * r
        keliling = 2 * math.pi * r
        hasil.set(f"Luas = {luas:.2f}, Keliling = {keliling:.2f}")
    except:
        messagebox.showerror("Error", "Input tidak valid")

# ======================
# KALKULATOR
# ======================
def tambah():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil = {a + b}")
    except:
        messagebox.showerror("Error", "Input salah")

def kurang():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil = {a - b}")
    except:
        messagebox.showerror("Error", "Input salah")

def kali():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil = {a * b}")
    except:
        messagebox.showerror("Error", "Input salah")

def bagi():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil = {a / b}")
    except:
        messagebox.showerror("Error", "Input salah / bagi 0")

# ======================
# TRIGONOMETRI
# ======================
def hitung_sin():
    sudut = float(entry1.get())
    hasil.set(f"sin = {math.sin(math.radians(sudut)):.3f}")

def hitung_cos():
    sudut = float(entry1.get())
    hasil.set(f"cos = {math.cos(math.radians(sudut)):.3f}")

def hitung_tan():
    sudut = float(entry1.get())
    hasil.set(f"tan = {math.tan(math.radians(sudut)):.3f}")

# ======================
# GUI
# ======================
root = tk.Tk()
root.title("Aplikasi Matematika")
root.geometry("400x500")

judul = tk.Label(root, text="Kalkulator & Bangun", font=("Arial", 16))
judul.pack(pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

hasil = tk.StringVar()
label_hasil = tk.Label(root, textvariable=hasil, font=("Arial", 12))
label_hasil.pack(pady=10)

# ======================
# BUTTON
# ======================
tk.Button(root, text="Persegi", command=hitung_persegi).pack(fill="x")
tk.Button(root, text="Persegi Panjang", command=hitung_persegi_panjang).pack(fill="x")
tk.Button(root, text="Lingkaran", command=hitung_lingkaran).pack(fill="x")

tk.Label(root, text="--- Kalkulator ---").pack()
tk.Button(root, text="Tambah", command=tambah).pack(fill="x")
tk.Button(root, text="Kurang", command=kurang).pack(fill="x")
tk.Button(root, text="Kali", command=kali).pack(fill="x")
tk.Button(root, text="Bagi", command=bagi).pack(fill="x")

tk.Label(root, text="--- Trigonometri ---").pack()
tk.Button(root, text="Sin", command=hitung_sin).pack(fill="x")
tk.Button(root, text="Cos", command=hitung_cos).pack(fill="x")
tk.Button(root, text="Tan", command=hitung_tan).pack(fill="x")

root.mainloop()