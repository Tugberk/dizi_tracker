import sqlite3
import datetime
from terminaltables import AsciiTable
#python3!

print("Bölüm takipçisi!")

def ask(son_id):
	print("Yeni dizi eklemek için 0 girin.")
	print("Yeni bölüm eklemek için dizi ID si girin - örnek:1")
	
	secenek = input(">> ")
		
	try:
		int(secenek)
	except:
		print("Lütfen bir sayı girin!")
		return ask(son_id) #burda return koymazsak eger devam ediyor calismaya ve hep bozuyordu 
		
	secenek = int(secenek)	
	if(secenek > son_id):
		return ask(son_id)
	return secenek

	

def main():
	#todays date
	now = datetime.datetime.now()
	tarih = str(now)[0:10]

	#lets connect to database
	con = sqlite3.connect("dizi.db")
	c = con.cursor()

	c.execute("select * from diziler")
	
	table_data = [
		['ID', 'Dizi Adı', 'Sezon', 'Son İzlenen Bölüm', 'Tarih']]
		

	new_list = [] #table_data yi duzgun bi formata sokmaya calisiyoruz

	while True:
		row = c.fetchone()
		if row == None:
			break
		
		dizi_id = str(row[0])
		dizi_adi = str(row[1])
		dizi_sezon = str(row[2])
		dizi_bolum = str(row[3])
		dizi_tarih = str(row[4])
		
		
		new_list.append(dizi_id)
		new_list.append(dizi_adi)
		new_list.append(dizi_sezon)
		new_list.append(dizi_bolum)
		new_list.append(dizi_tarih)
		table_data.append(new_list)
		new_list = []
		
		son_id = row[0] #dizinin oldugu sayidan buyuk sayi girdi mi anlayalim diye
		

	#tabular forma donusturup yazalım
	table = AsciiTable(table_data)
	print(table.table)	

	secenek = ask(son_id) #ask dan return ettigimiz degeri secenek e esitledik

	if(secenek == 0):
		print("yeni dizi")
		dizi_adi = input("Dizinin adı nedir?\n")
		sezon = input("Kaçıncı sezon?\n")
		son_bolum = input("Kaçıncı Bölüm?\n")
		print(dizi_adi, sezon, son_bolum)
		c.execute("insert into diziler(dizi_adi, sezon, son_izlenen, tarih) values(?,?,?,?)",(dizi_adi, sezon, son_bolum, tarih))
		con.commit()
		print("Eklendi!")
		
	else:
		c.execute("select * from diziler where id = ?", (secenek,)) #secenegin yanina virgul koyunca duzeldi
		con.commit()
		result = c.fetchone()
		son_bolum = input(result[1] +  " dizisi için son Bölüm Girin:  ")
		c.execute("update diziler set son_izlenen = ? where id = ?", (son_bolum, secenek))
		con.commit()
	
	main()
	
main()
