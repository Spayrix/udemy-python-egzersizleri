"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

"""

a = int(input("Birinci Sayıyı Giriniz: "))
b = int(input("İkinci Sayıyı Giriniz : "))
c = int(input("Üçüncü Sayıyı Giriniz : "))
multipy = a * b * c

print("Çarpım Sonucu: {} x {} x {} = {}".format(a,b,c,multipy))
