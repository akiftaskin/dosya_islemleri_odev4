import json
import os

# Dosya yoksa, boş bir listeyle oluştur
if not os.path.exists("kullanicilar.json"):
    with open("kullanicilar.json", "w", encoding="utf-8") as dosya:
        json.dump([], dosya, ensure_ascii=False, indent=4)

def kullanici_ekle():
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ") 
    yas = input("Yaşınızı girin: ")

    yeni_kullanici = {"ad": ad, "soyad": soyad, "yas": yas} 

    # Önce mevcut veriyi oku
    with open("kullanicilar.json", "r", encoding="utf-8") as dosya:
        kullanicilar = json.load(dosya)

    # Yeni kullanıcıyı listeye ekle
    kullanicilar.append(yeni_kullanici)

    # Güncellenmiş listeyi tekrar dosyaya yaz
    with open("kullanicilar.json", "w", encoding="utf-8") as dosya:
        json.dump(kullanicilar, dosya, ensure_ascii=False, indent=4)

    print("Kullanıcı başarıyla eklendi!\n")

def kullanicilari_listele():
    with open("kullanicilar.json", "r", encoding="utf-8") as dosya:
        kullanicilar = json.load(dosya)

    if kullanicilar:
        print("\nKayıtlı Kullanıcılar:")
        for kullanici in kullanicilar:
            print(f"Ad: {kullanici['ad']}, Soyad: {kullanici['soyad']}, Yaş: {kullanici['yas']}")  # Soyadı ekranda gösteriyoruz
    else:
        print("Henüz kayıtlı kullanıcı yok.\n")

# Ana döngü
while True:
    komut = input("Komut girin (ekle/listele/cikis): ").strip().lower()
    if komut == "ekle":
        kullanici_ekle()
    elif komut == "listele":
        kullanicilari_listele()
    elif komut == "cikis":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz komut! Lütfen 'ekle', 'listele' veya 'cikis' girin.")
