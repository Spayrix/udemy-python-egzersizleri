"""
Asal Sayılar : 1'e ve Kendisinden başka sayıya bölünemeyen sayılara denir.
"""

def asal_mi(sayi):
    if sayi < 2:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range (2,sayi):
            if sayi % i == 0:
                return False
        return True

while True:
    sayi = input("Sayı (Çıkmak için 'q'ya basınız) : ")

    if sayi == "q":
        print("Çıkış Yapılıyor...")
        break

    else:
        sayi = int(sayi)

        if asal_mi(sayi):
            print(sayi,"Asal Bir Sayıdır.\n")
        else:
            print(sayi,"Asal Bir Sayı Değildir.\n")







