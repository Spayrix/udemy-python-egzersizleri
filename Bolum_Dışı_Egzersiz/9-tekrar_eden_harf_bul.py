"""
En Çok Tekrar Eden Harf
Görev: Kullanıcının girdiği bir metindeki en çok tekrar eden harfi bul.

💡 İpucu: dict kullanarak harf sayıları tutulabilir.
"""
harf_sayilari = {}

metin = input("Lütfen Bir Metin Giriniz: ")

for harf in metin:
    harf = harf.lower()
    if harf in harf_sayilari:
        harf_sayilari[harf] += 1
    else:
        harf_sayilari[harf] = 1


en_cok_harf = max(harf_sayilari, key=harf_sayilari.get)

print("En Çok Tekrar Eden Harf: ",en_cok_harf)
print("Tekrar Sayısı: ",harf_sayilari[en_cok_harf])


