"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok
"""
""" 
def EBOB():
    sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
    sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))

    for i in range(min(sayi1, sayi2), 0, -1): # min(sayi1, sayi2); sayi1 ve sayi2'den küçük olanı alır , range(başlangıç, bitiş, adım)
        if sayi1 % i == 0 and sayi2 % i == 0:
            return i
        return None
    return None


print("EBOB: ",EBOB())
"""


def ebob_bulma(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:", ebob_bulma(sayı1, sayı2))