import os

def ekle():
    with open("rehber.txt", "a", encoding="utf-8") as dosya:
        ad = input("İsim: ")
        telefon = input("Telefon: ")
        dosya.write(f"{ad} - {telefon}\n")

def ara():
    aranan = input("Aranacak kişi: ")
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                if aranan in satir:
                    print("Bulundu:", satir.strip())
                    return
        print("Kişi bulunamadı!")
    else:
        print("Rehber dosyası yok!")

def listele():
    if os.path.exists("rehber.txt"):
        with open("rehber.txt", "r", encoding="utf-8") as dosya:
            print("\nRehber:")
            print(dosya.read())
    else:
        print("Rehber dosyası bulunamadı!")

def sil():
    if os.path.exists("rehber.txt"):
        os.remove("rehber.txt")
        print("Rehber tamamen silindi.")
    else:
        print("Rehber zaten yok.")

while True:
    komut = input("Komut (ekle/ara/listele/sil/çıkış): ")
    if komut == "ekle":
        ekle()
    elif komut == "ara":
        ara()
    elif komut == "listele":
        listele()
    elif komut == "sil":
        sil()
    elif komut == "çıkış":
        break
