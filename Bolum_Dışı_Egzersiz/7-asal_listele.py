"""
7. Asal Sayılar Listesi
Görev: 1 ile 100 arasındaki tüm asal sayıları listele.
İpucu: Her sayı için asal mı diye kontrol eden asal_mi() fonksiyonu yaz.
"""
asal_sayilar = []
def asal_mi(sayi):
        if sayi < 2:
            return False
        else:
            for i in range(2,sayi):
                if sayi % i == 0:
                    return False
            return True

for sayi in range(1,100):
    if asal_mi(sayi):
        asal_sayilar.append(sayi)

print("1 ile 100 arasındaki asal sayılar:", asal_sayilar)



