print("""
*******************************************
Bir Sayının Faktöriyelini Bulma Programı

Çıkmak İçin 'q'ya Basın
*******************************************
""")

while True:
    sayı = input("Sayı: ")
    if sayı == "q":
        print("Program Sonlandırılıyor")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2, sayı + 1):
            print("Faktöriyel:",faktoriyel,"ve i:",i)
            faktoriyel *= i

        print ("Faktöriyel: {}".format (faktoriyel))