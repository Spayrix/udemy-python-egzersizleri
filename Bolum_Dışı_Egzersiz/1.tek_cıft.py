"""
1. Sayı Tek mi Çift mi?
Görev: Kullanıcının girdiği bir sayının tek mi çift mi olduğunu ekrana yazdır.

💡 İpucu: % operatörünü kullan.
"""

print("Tek-Çift Bulma Programına Hoşgeldiniz.\n")
print("Çıkmak için 'q'ya Basınız.\n")



while True:
    sayı = input("Sayı Giriniz: ")

    if sayı == "q":
        print("Programdan Çıkılıyor...")
        break
    else:
        sayı = int(sayı)

        if sayı % 2 == 0:

            print("Bu Sayı Çifttir.\n")
        else:
            print("Bu Sayı Tektir.\n")