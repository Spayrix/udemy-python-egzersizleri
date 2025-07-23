print("""
******************************
Kullanıcı Girişi Programı
******************************
""")

sys_Kullanıcı_adi = "Mehmet"
sys_Parola = 12345
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adınızı Giriniz: ")
    parola = int(input("Parola Giriniz: "))
    if kullanıcı_adı != sys_Kullanıcı_adi and parola == sys_Parola:
        print("Kullanıcı Adını Yanlış Girdiniz\n")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkınız {}\n".format(giriş_hakkı))

    elif kullanıcı_adı == sys_Kullanıcı_adi and parola != sys_Parola:
        print("Parolayı Yanlış Girdiniz\n")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkınız {}\n".format(giriş_hakkı))

    elif kullanıcı_adı != sys_Kullanıcı_adi and parola != sys_Parola:
        print("Kullanıcı Adı ve Parolayı Yanlış Girdiniz\n")
        giriş_hakkı -= 1
        print("Kalan Giriş Hakkınız {}\n".format(giriş_hakkı))

    else:
        print("Giriş Başarıyla Yapıldı...\n")
        print("Hoşgeldiniz.")
        break

    if giriş_hakkı == 0:
        print("Giriş Hakkınız Bitti. Daha Sonra Tekrar Deneyiniz.")
        break

