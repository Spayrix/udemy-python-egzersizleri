print("""
****************************************
Atm Makinesine Hoşgeldiniz

İşlemler;

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q' ya basın.
****************************************
""")

bakiye = 1000
sys_şifre = 1234
hak = 3
kart_sahibi = "Mehmet"


while hak > 0:
    şifre = int(input("Lütfen 4 Haneli Kart Şifrenizi Giriniz: "))

    if şifre == sys_şifre:
        print("Hoşgeldiniz {} Bey.\n".format(kart_sahibi))
        break

    else:
        hak -= 1
        if hak == 0:
            print("Hakkınız Bitti! Lütfen Kartınızı Geri Alınız ve En Yakın Şubemize Başvurunuz.\n")
        else:
            print("Girilen 4 Haneli Kart Şifresi Yanlış\n")
            print("Kartınıza Bloke Konulmaması İçin Kalan Hakkınız {}\n".format(hak))




while True:
    işlem = input("\nLütfen Yapmak İstediğiniz İşlemi Seçiniz: ")

    if işlem == "q":
        print("Yine Bekleriz\n")
        break

    elif işlem == "1":
        print("Güncel Bakiyeniz {}TL'dir\n".format(bakiye))


    elif işlem == "2":
        yatırma_tutarı = int(input("\nLütfen Yatırmak İstediğiniz Tutarı Giriniz: "))
        bakiye += yatırma_tutarı
        print("Bakiyeniz {}TL'dir\n".format(bakiye))

    elif işlem == "3":
        çekme_tutarı = int(input("\nLütfen Çekmek İstediğiniz Tutarı Giriniz: "))

        if bakiye - çekme_tutarı < 0:
            print("Bakiyeniz Yetersiz.\n")
            print("Bakiyeniz {}TL'dir\n".format(bakiye))
            continue
        else:
            bakiye -= çekme_tutarı
            print("Bakiyeniz {}TL'dir\n".format(bakiye))

    else:
        print("Yanlış İşlemi Tuşladınız...\n")


