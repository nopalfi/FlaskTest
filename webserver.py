from flask import Flask
from flask import render_template
import sqlite3

conn=sqlite3.connect("database_test.db", check_same_thread=False)
c=conn.cursor()

app=Flask(__name__)

@app.route("/")
def index():
    c.execute("SELECT * FROM users")
    return render_template('index.html', rows = c.fetchall(), zip=zip)

@app.route("/absensi")
def absensi():
    c.execute("SELECT * FROM absensi")
    rowAbsensi = c.fetchall()
    id = rowAbsensi[0][1]
    c.execute("SELECT name, jabatan from users where id = ?",(id,))
    rowUsers = c.fetchall()
    return render_template('index.html', absensi = rowAbsensi, users = rowUsers, zip=zip)

if __name__ == '__main__':
    app.run()