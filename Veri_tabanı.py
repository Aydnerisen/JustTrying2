import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('DUNE','Frank Herbert','İthaki',467)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
"""    
isim = input("İsim:")
yazar = input("Yazar:")
yayınevi= input("Yayınevi:")
sayfa_sayısı= input("Sayfa Sayısı:")
veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
"""

def verileri_al():
    cursor.execute("Select* From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")

    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select isim,Yazar From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun isim ve yazar bilgileri...")
    for i in liste:
        print(i)
def veri_sec(yayınevi):
    cursor.execute("Select* From kitaplık where Yayınevi=?",(yayınevi,))
    liste = cursor.fetchall()
    print("Seçili yayınevi..")
    for i in liste:
        print(i)
"""
yayınevi = input("yayınevi:")
veri_sec(yayınevi)
"""

def veri_güncelleme(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set yayınevi=? where Sayfa_Sayısı=?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
"""
veri_güncelleme(999,"Ortak yayın")
verileri_al()
"""


def veri_sil(a):

    cursor.execute("Delete From kitaplık where Sayfa_Sayısı=?",(a))
    con.commit()

veri_sil("C")
verileri_al()
con.close()
