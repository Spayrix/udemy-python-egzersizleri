"""Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."""

a = int(input("Birinci Değeri Giriniz: "))
b = int(input("İkinci Değeri Giriniz: "))

print("Değiştirilmeden önceki değerler\na: {} b :{}".format(a, b))

a,b = b,a

print("Değiştirildikten sonraki değerler\na :{} b :{}".format(a, b))