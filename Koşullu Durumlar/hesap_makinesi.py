print("""
***************************************
*    Hesap Makinesi Programı          *
*                                     *
*    1.Toplama İşlemi                 *
*                                     *    
*    2.Çıkarma İşlemi                 *
*                                     *
*    3.Çarpma İşlemi                  *
*                                     *
*    4.Bölme İşlemi                   *
***************************************
""")
islem = input("İşlemi Giriniz: ")
a = int(input("Lütfen Birinci Sayıyı Giriniz: "))
b = int(input("Lütfen İkinci Sayıyı Giriniz: "))


if islem == "1":
    print("{} ile {} toplamı = {}".format(a, b, a+b))
elif islem == "2":
    print("{} ile {} farkı = {}".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} çarpımı = {}".format(a, b, a * b))
elif islem == "4":
    if b == 0:
        print("Bir sayı sıfıra bölünemez!")
    else:
        print("{} ile {} bölümü = {}".format(a, b, a / b))

else:
    print("Geçersiz işlem...")