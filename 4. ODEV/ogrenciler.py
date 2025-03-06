def ogrenci_ekle():
    while True:
        ogrenci = input("Eklemek istediğiniz öğrencinin adını girin (Bitirmek için 'bitti' yazın): ")
        if ogrenci.lower() == "bitti":
            break
        with open("ogrenciler.txt", "a", encoding="utf-8") as dosya:
            dosya.write(ogrenci + "\n")
        print("Öğrenci başarılı bir şekilde eklendi.")

def ogrencileri_goruntule():
    with open("ogrenciler.txt", "r", encoding="utf-8") as dosya:
        print("\nÖğrenci Listesi:")
        print(dosya.read())

ogrenci_ekle()
ogrencileri_goruntule()
