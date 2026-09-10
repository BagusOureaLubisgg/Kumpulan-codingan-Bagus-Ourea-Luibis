from flask import Flask, render_template, request, redirect, session
import json, os, re, bcrypt, time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretkey123"

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

def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email)

# ================= ROUTES =================
@app.route("/")
def home():
    return redirect("/login")

# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    users = load_users()

    if request.method == "POST":
        email = request.form["email"].lower()

        if not valid_email(email):
            return "Email tidak valid!"

        if email in users:
            return "Email sudah terdaftar!"

        password = request.form["password"]
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        nama = request.form["nama"]
        tempat = request.form["tempat"]
        tanggal = int(request.form["tanggal"])
        bulan = int(request.form["bulan"])
        tahun = int(request.form["tahun"])

        umur = hitung_umur(tahun, bulan, tanggal)

        users[email] = {
            "password": hashed,
            "failed": 0,
            "locked_until": 0,
            "profile": {
                "nama": nama,
                "tempat_lahir": tempat,
                "tanggal": tanggal,
                "bulan": bulan,
                "tahun": tahun,
                "umur": umur
            }
        }

        save_users(users)
        return redirect("/login")

    return render_template("register.html")

# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    users = load_users()

    if request.method == "POST":
        email = request.form["email"].lower()
        password = request.form["password"]

        user = users.get(email)

        if not user:
            return "Email atau password salah!"

        if time.time() < user["locked_until"]:
            return "Akun dikunci sementara!"

        if bcrypt.checkpw(password.encode(), user["password"].encode()):
            session["user"] = email
            user["failed"] = 0
        else:
            user["failed"] += 1
            if user["failed"] >= 3:
                user["locked_until"] = time.time() + 30
            save_users(users)
            return "Email atau password salah!"

        save_users(users)
        return redirect("/dashboard")

    return render_template("login.html")

# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    users = load_users()
    user = users.get(session["user"])

    return render_template("dashboard.html", data=user["profile"])

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)