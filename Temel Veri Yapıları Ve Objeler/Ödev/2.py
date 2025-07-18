"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""

print("Beden Kitle İndeksi Bulan Uygulamaya hoşgeldiniz.")

print("-------------------------------------------------")

boy = float(input("Lütfen boyunuzu **metre** cinsinden (örn: 1.75) giriniz: "))
kilo = int(input("Lütfen kilonuzu **kg** cinsinden (örn: 70) giriniz: "))

index = kilo / (boy ** 2)

print("Beden Kitle İndeksiniz: {:.2f}".format(index))


"""
hocanın yaptığı

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Beden Kitle İndeksi:",kilo / (boy ** 2))

"""