"""
3. 1’den 100’e kadar 3’e bölünen sayılar
Görev: 1–100 arasındaki 3’e tam bölünen sayıları yazdır.

💡 İpucu: continue kullanabilirsin.
"""

"""
for sayi in range(1 , 101):
    if sayi % 3 != 0:
        continue
    else:
        print(sayi)
"""

bolunenler = []

for sayi in range(1, 101):
    if sayi % 3 != 0:
        continue
    else:
        bolunenler.append(sayi)

print("3'e tam bölünen sayılar:", bolunenler)

