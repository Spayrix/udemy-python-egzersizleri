"""
2. Sayının Faktöriyeli
Görev: Girilen pozitif bir sayının faktöriyelini hesapla ve ekrana yazdır.

💡 İpucu: for döngüsü veya while ile 1’den n’e kadar çarp.
"""

print("Faktoriyel Programına Hoşgeldiniz.\n")
print("Çıkmak için 'q'ya Basınız.\n")



while True:
    sayı = input("Lütfen Bir Sayı Giriniz: ")

    if sayı == "q":
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2, sayı+1):
            print ("{} x {}".format(faktoriyel,i))
            faktoriyel *= i
            print("Faktöriyel: {}".format (faktoriyel))
            print()

