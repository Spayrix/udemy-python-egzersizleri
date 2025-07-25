"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;

abs(-4)
4
abs(5)
5
"""
şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz? (Üçgen, Dörtgen) :")

if şekil.lower() == "dörtgen":
    print("Lütfen Kenarları Sırayla Giriniz.")
    a = int(input("1-Kenar: "))
    b = int(input("2-Kenar: "))
    c = int(input("3-Kenar: "))
    d = int(input("4-Kenar: "))

    if a == b and a == c and a == d:
        print("Bu Bir Karedir")
    elif a == c and b == d:
        print("Bu Bir Dikdörtgendir")
    else:
        print("Bu Bir Sıradan Dörtgendir")

elif şekil.lower() == "üçgen":
    print("Lütfen Üçgenin Kenarlarını Sırayla Giriniz.")
    a = int(input("1-Kenar: "))
    b = int(input("2-Kenar: "))
    c = int(input("3-Kenar: "))
    if a + b > c and a + c > b and b + c > a:
        if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("Bu Bir İkizkenar Üçgendir")
        elif a == b and a == c:
            print("Bu Bir Eşkenar Üçgendir")
        else:
            print("Bu Sıradan Bir Üçgendir")
    else:
        print("Üçgen Belirtilmiyor...")
else:
    print("Geçersiz Şekil...")

