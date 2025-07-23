"""
4. Mükemmel Sayı
Görev: Girilen sayının mükemmel sayı olup olmadığını kontrol et.

💡 Tanım: Kendisinden küçük pozitif bölenlerinin toplamı kendisine eşitse.

ör : 1 + 2 + 3 = 6
"""

while True:
    bolenler = []
    sayi = input("\nLütfen Bir Sayı Giriniz (Çıkmak için 'q'ya Basınız): ")


    if sayi == "q":
        print("Programdan Çıkılıyor.")
        break
    else:

        sayi = int(sayi)
        toplam = 0
        for i in range (1,sayi):

            if sayi % i == 0 :
                toplam += i
                bolenler.append(i)


        if toplam == sayi:
            print("")
            print("{} Bir Mükemmel Sayıdır".format(sayi))
            print("Pozitif Bölenler: ", bolenler)
            print(" + ".join(str(i) for i in bolenler), "=", toplam)
        else:
            print("Bu Bir Mükemmel Sayı Değildir")
            continue





# Bunu gptle yaptık ama güzel görünüyor
          #  print("Pozitif Bölenlerin Toplamı = ".format(toplam)) --> Bu basit olan