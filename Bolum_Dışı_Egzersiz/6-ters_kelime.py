"""
6. Kelimeleri Tersten Yaz
Görev: Girilen cümledeki Kelimelerin Sırasını Ters Çevir

💡 İpucu: split(), [::-1], join() kullan.
"""

metin = input("Lütfen Bir Kelime Giriniz: ")

ters =" ".join(metin.split()[::-1])
print(ters)

