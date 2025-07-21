"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

while True:
    sayı = input("Bir Sayı Giriniz (Çıkmak için 'q'ya basın) : ")

    if sayı == "q":
        print("Programdan Çıkılıyor...")
        break
    else:
        basamak_sayısı = len(sayı)
        toplam = sum([int(i) ** basamak_sayısı for i in sayı])
        if toplam == int(sayı):
            print("Bu Bir Armstrong Sayısıdır")

        else:
            print("Bu Bir Armstrong Sayısı Değildir")







