import datetime
import time
import os

def log_ekle(mesaj):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{zaman} - {mesaj}\n")

def loglari_goruntule():
    if os.path.exists("log.txt"):
        with open("log.txt", "r", encoding="utf-8") as dosya:
            print("\nLog Kayıtları:")
            print(dosya.read())
    else:
        print("Henüz log kaydı yok.\n")

def otomatik_log():
    try:
        while True:
            log_ekle("Sistem aktif durumda.")
            time.sleep(10)  # Her 10 saniyede bir log kaydı
    except KeyboardInterrupt:
        print("\nOtomatik loglama durduruldu.")

# Ana menü
while True:
    komut = input("Komut girin (baslat/goruntule/cikis): ").strip().lower()

    if komut == "baslat":
        print("Otomatik loglama başlatılıyor. Durdurmak için CTRL+C yapın.")
        otomatik_log()
    elif komut == "goruntule":
        loglari_goruntule()
    elif komut == "cikis":
        print("Log programından çıkılıyor.")
        break
    else:
        print("Geçersiz komut! Lütfen 'baslat', 'goruntule' veya 'cikis' girin.\n")
