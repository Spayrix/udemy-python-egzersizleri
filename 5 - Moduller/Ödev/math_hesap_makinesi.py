"""
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
"""
import math
import time

def menu():
    while True:

        print("""
                ***********************************

                1 - Karekök
                2 - Üs Alma
                3 - Logaritma
                4 - Faktöriyel
                5 - EBOB 
                6 - Yukarı Aşağı Yuvarlama
                7 - Derece ↔ Radyan dönüşümü       

                *********************************** 
                """)

        secim = input("\nLütfen Yapmak İstediğiniz İşlemi Seçiniz(Çıkmak İçin 'q'ya basınız.): ")




        if secim == 'q':
            print("Çıkış Yapılıyor...")
            time.sleep(1)
            break
        elif secim == '1':
            x = float(input("Karekök Alınacak Sayıyı Giriniz: "))
            print("Sonuç: ",math.sqrt(x))

        elif secim == '2':
            x = float(input("Taban Değeri Giriniz: "))
            y = float(input("Üs Değeri Giriniz: "))
            print("Sonuç: ",math.pow(x,y))

        elif secim == '3':
            x = float(input("Logaritması Alınacak Sayıyı Giriniz: "))
            y = float(input("Taban Değeri Giriniz: "))
            print("Sonuç: ",math.log(x,y))

        elif secim == '4':
            x = int(input("Faktöriyeli Alınacak Sayıyı Giriniz: "))
            print("Sonuç: ",math.factorial(x))

        elif secim == '5':
            x = int(input("Birinci Sayıyı Giriniz: "))
            y = int(input("İkinci Sayıyı Giriniz: "))
            print("Sonuç: ",math.gcd(x,y))

        elif secim == '6':
            secenek = input("Yuvarlama yönü (aşağı/yukarı): ").strip().lower()

            if secenek == 'aşağı':
                 x = float(input("Aşağı Yuvarlamak İstediğiniz Sayıyı Giriniz: "))
                 print("Sonuç: ",math.floor(x))


            elif secenek == 'yukarı':
                x = float(input("Yukarı Yuvarlamak İstediğiniz Sayıyı Giriniz: "))
                print("Sonuç: ",math.ceil(x))


            else:
                print("Yanlış Tuşlama Yaptınız Lütfen Tekrar Deneyiniz.")

        elif secim == '7':
            x = float(input("Açı Giriniz: "))
            print("Radyan: ",math.radians(x))
            print("Derece: ",math.degrees(x))

        else:
            print("Geçersiz giriş yaptınız. Tekrar deneyin.")

print("Hesap Makinesi Programımıza Hoşgeldiniz...\n")
time.sleep(1)
menu()