"""
Sayı Tahmin Oyunu
Görev: Bilgisayarın rastgele tuttuğu sayıyı 5 denemede tahmin etmeye çalış.

💡 İpucu: random.randint(1,100) ile sayı üret, kullanıcıdan tahmin al.
"""
import random

sayi = random.randint(1,100)



while True:
    tahmin = input("\nTahmin (Çıkmak için 'q'ya Basınız):  ")
    if tahmin == "q":
        break
    else:
        tahmin = int(tahmin)
        if tahmin == sayi:
            print("Tebrikler Sayımız {} Doğru bildiniz".format(sayi))
        else:
            print("Tekrar Dene ! ")
            ilk_rakam = str(sayi)[0]
            print("İpucu Sayı {} İle Başlıyor.".format(ilk_rakam))
            continue



