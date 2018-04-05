import sqlite3

con = sqlite3.connect("dizi.db")
c = con.cursor()

c.execute("create table diziler(id INTEGER PRIMARY KEY AUTOINCREMENT, dizi_adi TEXT NOT NULL, sezon INT NOT NULL, son_izlenen INT NOT NULL, tarih datetime)")
con.commit()

