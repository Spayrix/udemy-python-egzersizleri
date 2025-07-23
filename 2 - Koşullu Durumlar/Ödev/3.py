"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
    """
Vize1 = int(input("İlk Vize Notunuzu Giriniz: "))
Vize2 = int(input("İkinci Vize Notunuzu Giriniz: "))
Final = int(input("Final Notunuzu Giriniz: "))
Toplam = (Vize1*0.3)+(Vize2 *  0.3) + (Final * 0.4)

if Toplam >= 90:
    print("Notunuz AA'dır")
elif Toplam >= 85:
    print("Notunuz BA'dır")
elif Toplam >= 80:
    print("Notunuz BB'dir")
elif Toplam >= 75:
    print("Notunuz CB'dir")
elif Toplam >= 70:
    print("Notunuz CC'dir")
elif Toplam >= 65:
    print("Notunuz DC'dir")
elif Toplam >= 60:
    print("Notunuz DD'dir")
elif Toplam >= 55:
    print("Notunuz FD'dir")
else :
    print("Notunuz FF'dir")