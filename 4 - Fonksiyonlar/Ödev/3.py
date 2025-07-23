"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""
"""
EKOK = 0
def EKOK_bul():
    sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
    sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))

    i = max(sayi1, sayi2)
    while True:
        if i % sayi1 == 0 and i % sayi2 == 0:
            return i
        i += 1

print("EKOK Değeri: ",EKOK_bul())
"""


def ekok_bulma(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:", ekok_bulma(sayı1, sayı2))