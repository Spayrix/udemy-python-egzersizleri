"""
Bir sayının tam bölenleri, o sayıyı kalansız (yani bölümünde kalan 0 olacak şekilde) bölebilen sayılardır.
Başka bir deyişle, bir sayı başka bir sayıya bölündüğünde sonuç tam sayı çıkıyorsa, bu sayı onun tam bölenidir.

Örneğin:

12 sayısının tam bölenleri:
1, 2, 3, 4, 6, 12
Çünkü 12 bu sayıların her biriyle bölündüğünde kalansız sonuç verir.

Bir Sayının Tam Bölenlerini Bulan Program Yazınız
"""

def tam_bolenleri(sayi):
   bolenler = []
   for i in range(1, sayi + 1):
        if sayi % i == 0:
            bolenler.append(i)
   return bolenler


while True:
    sayi = input("\nSayı Giriniz (Çıkmak İçin 'q'ya basınız): ")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        if tam_bolenleri(sayi):
            print("Bu Sayının Tam Bölenler: ",tam_bolenleri(sayi))
        else:
            print("Lütfen Pozitif Bir Sayı Giriniz.")