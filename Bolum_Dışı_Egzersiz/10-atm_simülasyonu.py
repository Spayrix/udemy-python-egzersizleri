"""
10. ATM Simülasyonu
Görev: Kullanıcının para yatırabildiği, çekebildiği, bakiye görüntüleyebildiği bir menü sistemi oluştur.

💡 İpucu: while True, input(), koşullar, fonksiyonlarla parçalara ayır.
"""
kullanicilar = {
    "mehmet" : "1234",
    "samet" : "4321",
    "emin" : "0000",
    "engin" : "1234",
    "salim" : "5432"
}

def giris():
    for hak in range(3,0,-1):
        kullanici_adi = input("Kullanıcı Adı: ").lower()
        sifre = input("Şifre: ")

        if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:
            print("Giriş Başarılı. Hoşgeldiniz.")
            return kullanici_adi
        else:
            print(f"Hatalı giriş. Kalan deneme hakkı: {hak - 1}")
    print("3 Kez Hatalı Giriş Yapıldı. Sistemden Çıkılıyor.")
    return None

def menu():
    bakiye = 1000
    while True:
        print("""
        1.Bakiye Sorgulama
        2. Para Yatırma
        3. Para Çekme
        4. Çıkış
        """)
        secim = input("Lütfen Seçiminizi Tuşlayınız: ")

        if secim == "1":
            print("Güncel Bakiyeniz = {}".format(bakiye))

        elif secim == "2":
            miktar = int(input("Lütfen Yatırmak İstediğiniz Bakiyeyi Giriniz: "))
            bakiye += miktar

        elif secim == "3":
            miktar = int(input("Lütfen Çekmek İstediğiniz Bakiyeyi Giriniz: "))
            if miktar <= bakiye:
                bakiye -= miktar
            else:
                print("Yetersiz Bakiye.")
        elif secim == "4":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Seçim")


kullanici = giris()
if kullanici:
    menu()


