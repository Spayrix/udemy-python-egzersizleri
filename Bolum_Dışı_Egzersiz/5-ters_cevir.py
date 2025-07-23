"""
5. Ters Çevirme
Görev: Kullanıcının girdiği sayıyı ters çevir (123 → 321).

💡 İpucu: Sayıyı önce str() yapıp, sonra [::-1] kullanabilirsin.

"""

while True:
    sayi = input("Lütfen Bir Sayı Giriniz (Çıkmak İçin 'q'ya Basınız): ")
    if sayi == "q":
        break
    else:
        print(sayi[::-1])
