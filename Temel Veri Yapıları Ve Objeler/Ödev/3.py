"""
Bir aracın kilometrede ne kadar yaktığı ve
kaç kilometre yol yaptığı bilgilerini alın ve
sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

"""

tüketim = float(input("Aracın kilometrede ne kadar yaktığını girin (TL): "))
mesafe = float(input("Aracınızın kat ettiği yolu km olarak (örn: 50) giriniz: "))
toplam = tüketim * mesafe

print("Toplam ödemeniz gereken tutar: {:.2f} TL".format(toplam))

