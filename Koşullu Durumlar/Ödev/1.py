"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

boy = float(input("Lütfen boyunuzu **metre** cinsinden (örn: 1.75) giriniz: "))
kilo = int(input("Lütfen kilonuzu **kg** cinsinden (örn: 70) giriniz: "))
index = kilo / (boy * boy)

if index <= 18.5:
    print("Zayıf")

elif 18.5 <= index <= 25:
    print("Normal")

elif 25 <= index <= 30:
    print("Fazla Kilo")

elif index >= 30:
    print("Obez")