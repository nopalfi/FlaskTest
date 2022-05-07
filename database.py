import sqlite3
from datetime import date, datetime

conn = sqlite3.connect("database_test.db")

if (conn):
    print("Database connected")

c=conn.cursor()

# sql = """
#         DROP TABLE IF EXISTS users;
#         CREATE TABLE users (
#             id integer primary key autoincrement,
#             username text,
#             name text,
#             jabatan text,
#             entry_date text
#         );

#         DROP TABLE IF EXISTS absensi;
#         CREATE TABLE absensi (
#             id integer primary key autoincrement,
#             users_id int NOT NULL,
#             suhu double,
#             date text,
#             FOREIGN KEY (users_id) REFERENCES users(id)
#         )
#         """

# c.executescript(sql)
# conn.commit()

if (c):
    print ("Table created")

def register_user():
    print("Username : ", end='')
    username = input()
    print("Nama Lengkap : ", end='')
    name = input()
    print("Jabatan : ", end='')
    jabatan = input()
    now = datetime.now()
    entry_date = now.strftime("%d/%m/%Y %H:%M:%S")
    
    c.execute("SELECT username from users where username = ?",(username,))
    check = c.fetchall()
    if len(check) == 0:
        c.execute("INSERT INTO users (username, name, jabatan, entry_date) VALUES (?,?,?,?)",(username,name,jabatan,entry_date))
        conn.commit()
        print("Commit success")
    else:
        print("Username sudah ada. Coba lagi!")
        pass

def entry_absensi():
    print("Users id: ",end='')
    users_id = input()
    print("Suhu: ", end='')
    suhu = input()
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    c.execute("SELECT id from users where id = ?",(users_id))
    check = c.fetchall()
    print (len(check))
    if len(check)==1:
        c.execute("INSERT INTO absensi (users_id, suhu, date) VALUES (?,?,?)",(users_id, suhu, date))
    else:
        print("Users id tidak ditemukan")
        pass


def checkdb():
    c.execute("SELECT * from users")
    rows = c.fetchall()
    for row in rows:
        print(row)


try:
    while True:
        # register_user()
        entry_absensi()
        checkdb()


except KeyboardInterrupt:
    conn.commit()
    c.close()
    conn.close()
