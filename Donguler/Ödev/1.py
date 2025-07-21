"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""




while True:
    sayı = input("Lütfen Sayı Giriniz (Çıkmak için q): ")

    if sayı.lower() == "q":
        print("Programdan Çıkılıyor...")
        break

    sayı = int(sayı)
    toplam = 0

    for i in range(1,sayı):
        if sayı % i == 0:
            toplam += i

    if toplam == sayı:
        print("Bu bir mükemmel sayıdır.")

    else:
        print("Bu bir mükemmel sayı değildir.")

