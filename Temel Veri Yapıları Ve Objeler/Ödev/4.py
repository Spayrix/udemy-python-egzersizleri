"""Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın."""

ad = input("Lütfen İsminizi Giriniz: ")
soyad = input("Lütfen Soyisminizi Giriniz: ")
numara = input("Lütfen Telefon Numaranızı Giriniz: ")

print("\nBilgiler...\n")
print("{}\n{}\n{}\n".format(ad, soyad, numara))