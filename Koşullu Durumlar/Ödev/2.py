"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
a = int(input("Birinci Sayıyı Giriniz: "))
b = int(input("İkinci Sayıyı Giriniz: "))
c = int(input("Üçüncü Sayıyı Giriniz: "))

if a > b and a > c:
    print("En büyük sayı {}".format(a))
elif b > a and b > c:
    print("En büyük sayı {}".format(b))
else:
    print("En büyük sayı {}".format(c))