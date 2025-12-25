import os
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect
from datetime import datetime, timedelta


app = Flask(__name__)

DB = "guardian.db"

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"  # Windows
REDIRECT_IP = "127.0.0.1"


def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY,
            site TEXT UNIQUE,
            unblock_time TEXT
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS app_blocks (
            id INTEGER PRIMARY KEY,
            app_name TEXT
        )
        """)



def block_site(site):
    variants = [
        site,
        f"www.{site}",
        f"m.{site}"
    ]

    with open(HOSTS_PATH, "r") as file:
        existing = file.read()

    with open(HOSTS_PATH, "a") as file:
        for v in variants:
            ipv4 = f"127.0.0.1 {v}"
            ipv6 = f"::1 {v}"

            if ipv4 not in existing:
                file.write(f"\n{ipv4}")
            if ipv6 not in existing:
                file.write(f"\n{ipv6}")






def unblock_site(site):
    with open(HOSTS_PATH, "r") as file:
        lines = file.readlines()
    with open(HOSTS_PATH, "w") as file:
        for line in lines:
            if site not in line:
                file.write(line)





@app.route("/", methods=["GET", "POST"])
def dashboard():
    init_db()
    now = datetime.now()

    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

        if request.method == "POST":
            site = request.form["site"]
            days = int(request.form["days"])
            unblock_time = now + timedelta(days=days)

            cursor.execute(
            "INSERT OR IGNORE INTO blocks (site, unblock_time) VALUES (?, ?)",
            (site, unblock_time.isoformat())
            )

            block_site(site)
            conn.commit()

        cursor.execute("SELECT * FROM blocks")
        blocks = cursor.fetchall()

        for block in blocks:
            unblock_time = datetime.fromisoformat(block[2])
            if now >= unblock_time:
                unblock_site(block[1])
                cursor.execute("DELETE FROM blocks WHERE id = ?", (block[0],))
                conn.commit()

    with sqlite3.connect(DB) as conn:
        apps = conn.execute("SELECT app_name FROM app_blocks").fetchall()


    return render_template("dashboard.html", blocks=blocks, apps=apps)





@app.route("/block_app", methods=["POST"])
def block_app():
    app_name = request.form["app_name"]

    with sqlite3.connect(DB) as conn:
        conn.execute(
            "INSERT INTO app_blocks (app_name) VALUES (?)",
            (app_name,)
        )
        conn.commit()

    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)
