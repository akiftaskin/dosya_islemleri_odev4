import os

def gunluk_yaz():
    not_metni = input("Günlüğünüze eklemek istediğiniz metni girin: ")
    with open("gunluk.txt", "a", encoding="utf-8") as dosya:
        dosya.write(not_metni + "\n")
    print("Not başarılı bir şekilde eklendi.")

def gunluk_goruntule():
    if os.path.exists("gunluk.txt"):
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            print("\nGünlük Notları:")
            print(dosya.read())
    else:
        print("Henüz günlük kaydı bulunmuyor.")

def gunluk_sil():
    if os.path.exists("gunluk.txt"):
        os.remove("gunluk.txt")
        print("Günlük başarıyla silindi.")
    else:
        print("Silinecek günlük bulunamadı.")

# Örnek çalışma:
while True:
    komut = input("Komut girin (yaz/goruntule/sil/cikis): ").strip().lower()
    if komut == "yaz":
        gunluk_yaz()
    elif komut == "goruntule":
        gunluk_goruntule()
    elif komut == "sil":
        gunluk_sil()
    elif komut == "cikis":
        print("Günlük programından çıkılıyor.")
        break
    else:
        print("Geçersiz komut!")
