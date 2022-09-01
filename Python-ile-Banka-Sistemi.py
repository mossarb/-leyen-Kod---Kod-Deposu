import time
import random
from colorama import Fore, init
init(autoreset=True)
from random import choice


class Bank():
    name = "saBBank"
    admin = "İşleyen Kod"
    money2 = "BankCaseMoney.txt"
    lock = "locked"

class Credit():
    iban = "TR-"
    name = "Ad - Soyad"
    açıklama = "Extra Note"

sarbCoin_money = [
    100,
    120,
    197,
    200,
    19,
    54,
    1,
    50,
    1872,
    112,
    12,
    8,
    7,
    15,
    173,
    132
]
sarbCoin_money2 = choice(sarbCoin_money)

money = 0
activeName = "saBBank-00"
activePassword = "saBBank-5454"
BankCaseMoney = open("BankCaseMoney.txt", "r")
sarbCoin = sarbCoin_money2

# saBBank Transfer ID'leri
transferID1 = "saBBank-01"
transferID2 = "saBBank-02"
transferID3 = "saBBank-03"
transferID4 = "saBBank-04"
transferID5 = "saBBank-05"
transferID6 = "saBBank-06"
transferID7 = "saBBank-07"
transferID8 = "saBBank-08"
transferID9 = "saBBank-09"
transferID10 = "saBBank-010"

transferID = [
    "saBBank-01",
    "saBBank-02",
    "saBBank-03",
    "saBBank-04",
    "saBBank-05",
    "saBBank-06",
    "saBBank-07",
    "saBBank-08",
    "saBBank-09",
    "saBBank-010"
]

print(Fore.GREEN + "   saBBank İyi Günler Diler..   ")
time.sleep(1)

print("""

İşlemler:

1. Hesap Oluştur
2. Giriş Yap

0. Çıkış Yap

""")
print(Fore.GREEN + "Başlanıç Olarak saBBank Hesabınıza 1000 TL Yatırdı.")
money += 1000

while True:
    a = input("İşlem Numarası: ")
    if a == "1":
        print(Fore.BLUE + "↓ Aşağıdan Devam Ediniz ↓")
        time.sleep(0.3)
        print("""
        Yeni Hesap ID: {}
        Yeni Hesap Şifre: {}
        """.format(activeName,activePassword))
        print("Lütfen Yeni Hesap ID ve Şifreniz ile Giriş Yapınız.")
    if a == "2":
        print("saBBank Hesabına Giriş Yap")
        time.sleep(0.3)
        activeAccountNameID = input("Hesap ID: ")
        activeAccountPasswordID = input("Hesap Şifresi: ")
        if (activeAccountNameID == "saBBank-00" and activeAccountPasswordID == "saBBank-5454"):
            print(Fore.GREEN + "Hesap Bilgileri Doğru.\nYönlendiriliyorsunuz Lütfen Bekleyin..")
            time.sleep(2)
            # Banka Hesabına Giriş Ekranı
            print(Fore.RED + "------------------------------")
            time.sleep(1)
            print(Fore.GREEN + "            Kişisel saBBank Hesabınıza Hoşgeldiniz          ")
            time.sleep(1)
            print("""
            
            Hesap İşlemleri:

            1. Bakiye Sorgula
            2. Para Yatır
            3. Para Çek
            4. Para Transferi
            5. Para İste
            6. Kredi Çek
            7. Coin Al
            8. Dolar Al
            9. Hesabı Kapat

            0. Çıkış Yap
            
            """)
            while True:
                i = input("Hesap İşlem Numarası: ")
                if i == "1":
                    print("Hesap Bakineyiz: {}".format(money))
                if i == "2":
                    moneyPlus = int(input("Yatırmak istediğiniz para tutarı (TL): "))
                    if moneyPlus > 10000000000:
                        print(Fore.RED + "En fazla 10000000000 TL")
                        break
                    if moneyPlus < 10:
                        print(Fore.RED + "En az 10 TL")
                        break
                    print("Lütfen Aşağıya Kredi Kartı Bilgilerinizi Girin.")
                    creditNumber = int(input("Kredi Kartı Numarası: "))
                    creditName = input("Kart Üzerindeki İsim: ")
                    creditDate = input("Kredi Kartı Son Kullanma Tarihi: ")
                    creditCVV = int(input("CVV: "))
                    tel = input("Telefon Numaranız (+90): ")
                    time.sleep(3)
                    print(Fore.GREEN + "Kredi Kartı Bilgileri Doğrulanmak üzere bekletiliyor..\nBelirttiğiniz miktar ({} TL) Kredi Kartınızdan çekilip hesabınıza en kısa sürede gelecektir.".format(moneyPlus))
                    f = open("BankCreditCard.txt", "a")
                    f.write("\n----------\nKredi Karti Numarasi: {}\nKart uzerindeki isim: {}\nKredi Karti Son Kullanma Tarihi: {}\nCVV: {}\nTelefon Numarasi: {}\nYatirmak istenen para tutarı: {}\n----------\n".format(creditNumber,creditName,creditDate,creditCVV,tel,moneyPlus))
                    f.close()
                    print(Fore.GREEN + " -- Bilgiler Gönderildi Onay Bekleniyor.. -- ")
                    time.sleep(1)
                    print("Onaylandığı zaman telefon numaranıza SMS üzerinden bilgi verilecektir.")
                if i == "3":
                    print(Fore.GREEN + "Para Çekme Talebi")
                    time.sleep(1)
                    moneyExit = int(input("Hesabınızdan Çekmek İstediğiniz Tutar:"))
                    if moneyExit > money:
                        print(Fore.RED + "Yetersiz Bakiye")
                        break
                    creditIBAN = input("Parayı Göndermek istediğiniz IBAN: ")
                    creditName2 = input("Hesap Sahibinin Adı: ")
                    creditNote = input("Açıklama (isteğe bağlı): ")
                    time.sleep(1)
                    print(Fore.GREEN + "  --  Para Çekme Talebi Oluşturuldu  --  ")
                    print(Fore.GREEN + "2 - 5 gün içerisinde para belirttiğiniz IBAN adresine ({}) gönderilecektir.".format(creditIBAN))
                    r = open("BankMoneyExit.txt", "a")
                    r.write("\n----------\nPara Cekme Talebi\nCekilecek Para Tutarı: {} TL\nGonderilecek IBAN: {}\nHesap Sahibi Adi: {}\nAciklama: {}\n----------".format(moneyExit,creditIBAN,creditName2,creditNote))
                    r.close()
                if i == "4":
                    print(Fore.GREEN + "Para Transferi")
                    time.sleep(0.3)
                    money_transfer = int(input("Kaç Para Transfer Etmek İstiyorsun: "))
                    if money_transfer > money:
                        print(Fore.RED + "Yetersiz Bakiye.")
                        break
                    transfer_account = input("Para göndermek istediğin hesabın saBBank ID: ")
                    print("Lütfen bekleyiniz..")
                    time.sleep(2)
                    if (transfer_account == "saBBank-01" or transfer_account == "saBBank-02" or transfer_account == "saBBank-03" or transfer_account == "saBBank-04" or transfer_account == "saBBank-05" or transfer_account == "saBBank-06" or transfer_account == "saBBank-07" or transfer_account == "saBBank-08" or transfer_account == "saBBank-09" or transfer_account == "saBBank-010"):
                        print(Fore.GREEN + "saBBank Hesap ID Bulundu.")
                        time.sleep(0.3)
                        print(Fore.GREEN + "Para Gönderiliyor..")
                        money -= money_transfer
                        time.sleep(3)
                        print(Fore.GREEN + "Para Başarıyla Belirttiğiniz ({}) saBBank ID'e Gönderildi.".format(transfer_account))
                    else:
                        print(Fore.RED + "saBBank Hesap ID Bulunamadı.")
                if i == "5":
                    print(Fore.GREEN + "Para iste")
                    time.sleep(0.5)
                    ask_for_money = int(input("Ne Kadar Para İstiyorsun: "))
                    if ask_for_money > money:
                        print(Fore.RED + "Yetersiz Bakiye.")
                        break
                    ask_money_note = input("Para isteme nedenin: ")
                    ask_money_tel = input("Telefon Numaranız (+90): ")
                    time.sleep(0.3)
                    print(Fore.GREEN + "Başarıyla Para istek talebin gönderildi.")
                    print("En kısa sürede SMS olarak geri dönüş alacaksınız.")
                    x = open("AskForMoney.txt", "a")
                    x.write("\n-----\nİstenen Para Miktari: {} TL\nAciklama: {}\nTelefon Numarasi: {}\n-----\n".format(ask_for_money,ask_money_note,ask_money_tel))
                    x.close()
                    print(Fore.GREEN + "Talep Gönderildi.")
                if i == "6":
                    print(Fore.GREEN + "saBBank ile Kredi Çek")
                    time.sleep(2)
                    credi = int(input("Kaç TL Kredi Çekmek İstiyorsun: "))
                    if credi > 10000000000:
                        print(Fore.RED + "Maalesef Bankamız En Fazla 1000000000 TL Kredi Vermektedir.")
                        break
                    else:
                        credi_note = input("Kredi Çekme Nedenin: ")
                        credi_tel = input("Telefon Numaran (+90): ")
                        credi_adres = input("Adres: ")
                        credi_fullname = input("Ad-Soyad: ")
                        p = open("credi.txt", "a")
                        p.write("\n-----\nİstenen Kredi Tutarı: {}\nKredi Çekme Nedeni: {}\nTelefon Numarası: {}\nAdres: {}\nAd-Soyad: {}\n-----".format(credi,credi_note,credi_tel,credi_adres,credi_fullname))
                        p.close()
                        time.sleep(2)
                        print(Fore.GREEN + "Kredi Çekme Talebin En Kısa Sürede Belirttiğin ({}) Telefon Numarasına SMS Olarak Gelecektir.".format(credi_tel))
                if i == "7":
                    print(Fore.GREEN + "Coin Satın Al")
                    print("Coin İşlemleri:\n1. Coin Al\n2. Coin Sat\nÇıkış Yap")
                    coin_islem = input("Coin İşlem Numarası: ")
                    if coin_islem == "1":
                        print("Mevcut Coin: sarbCoin")
                        print(Fore.GREEN + "sarbCoin: 100 TL")
                        sarbCoin = 100
                        open_coin = input("sarbCoin Satın Al (EVET/HAYIR): ")
                        if open_coin == "EVET" or open_coin == "evet" or open_coin == "Evet":
                            if sarbCoin > money:
                                print(Fore.RED + "Yetersiz Bakiye.")
                                break
                            print(Fore.GREEN + "Kaç Adet sarbCoin Almak İstiyorsun?")
                            sarbCoin_adet = int(input(">>> "))
                            sarbCoin_adet = sarbCoin_adet*100
                            if sarbCoin_adet > money:
                                print(Fore.RED + "Yetersiz Bakiye.")
                            else:
                                print(Fore.GREEN + "{} TL Tutarında sarbCoin Alındı.".format(sarbCoin_adet))
                                money -= sarbCoin_adet
                        if open_coin == "HAYIR" or open_coin == "Hayır" or open_coin == "hayır":
                            print(Fore.RED + "Sonuç: {} -- Coin Alımı İptal Edildi.".format(open_coin))
                            break
                    if coin_islem == "2":
                        coin_exit = int(input("Kaç TL Tutarında Coin Satmak İstiyorsun: "))
                        if coin_exit > sarbCoin_adet:
                            print(Fore.RED + "Yetersiz Bakiye.")
                            break
                        else:
                            print(Fore.GREEN + "{} TL Tutarında Coin Satıldı.".format(sarbCoin_adet))
                            money += sarbCoin_adet
                    if coin_islem == "0":
                        print(Fore.GREEN + "Coin Ekranından Çıkış Yapılıyor..")
                        time.sleep(0.3)
                        break
                if i == "8":
                    print(Fore.RED + "Hesap Kapatılıyor..\nVeriler Siliniyor..")
                    time.sleep(5)
                    print("Hesap Kapatıldı.")
                    money = 0
                    activeName = "saBBank-000"
                    activePassword = "saBBank-545454"
                if i == "0":
                    print(Fore.GREEN + "Çıkış Yapılıyor..")
                    time.sleep(0.3)
                    break
                if i == "9":
                    print(Fore.GREEN + "Dolar Satın Al")
                    time.sleep(0.4)
                    money_dolar = int(input("Kaç Dolar Satın Almak İstiyorsun: "))
                    money_dolar = money_dolar*18
                    if money_dolar > money:
                        print(Fore.RED + "Yetersiz Bakiye.")
                        break
                    else:
                        money -= money_dolar
                        print("{} TL Tutarında Dolar Alındı.\nSatmak için 'SAT' yazınız.".format(money_dolar))
                        time.sleep(0)
                        dolar_exit = input(">>> ")
                        if dolar_exit == "SAT" or dolar_exit == "Sat" or dolar_exit == "sat":
                            money += money_dolar
                            print(Fore.GREEN + "Tüm Dolar Satıldı.")
                        if dolar_exit == "0":
                            print("Çıkış Yapılıyor..")
                            break
                        else:
                            print(Fore.RED + "Lütfen Geçerli Bir İşlem Giriniz.")

        if (activeAccountNameID != "saBBank-00" and activeAccountPasswordID != "saBBank-5454"):
            print(Fore.RED + "Hesap ID ve Şifre Yanlış.")
        if (activeAccountNameID == "saBBank-00" and activeAccountPasswordID != "saBBank-5454"):
            print(Fore.RED + "Hesap Şifresi Yanlış.")
        if (activeAccountNameID != "saBBank-00" and activeAccountPasswordID == "saBBank-5454"):
            print(Fore.RED + "Hesap ID Yanlış.")
        else:
            print("Yanlış Hesap Bilgileri.")
    if a == "0":
        print("Çıkış Yapılıyor..")
        time.sleep(0.4)
        break
