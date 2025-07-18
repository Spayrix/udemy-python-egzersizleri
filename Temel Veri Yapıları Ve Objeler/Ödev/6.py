"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""
a = int(input("Birinci Dik Kenarı Giriniz: "))
b = int(input("İkinci Dik Kenarı Giriniz: "))
c = (a**2 + b**2) ** 0.5
print("Hipotenüs: ",c)