import random
import time

print("""
******************************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.


******************************************
""")
rastgele_sayi = random.randint(1, 40)
tahmin_hakki = 2
while tahmin_hakki > 0:
    tahmin = int(input("\nTahmininiz: "))
    if tahmin < rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Yüksek Bir Sayı Giriniz.")
        tahmin_hakki -= 1
        print("Kalan Tahmin Hakkınız: ", tahmin_hakki)

    elif tahmin > rastgele_sayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha Düşük Bir Sayı Giriniz.")
        tahmin_hakki -= 1
        print("Kalan Tahmin Hakkınız: ",tahmin_hakki)

    else:
        print("Tebrikler Sayıyı Doğru Tahmin Ettiniz.")
        break

    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Kalmadı")
        print("Sayımız: ", rastgele_sayi)
        print("\nProgramdan Çıkılıyor...")
        time.sleep(1)
        break
