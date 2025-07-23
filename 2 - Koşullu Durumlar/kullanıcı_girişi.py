print("""
**************************
    Kullanıcı Girişi
**************************
""")

sys_Kullanici_adi = "Mehmet"
sys_parola = "12345"

Kullanici_adi = input("Kullanıcı Adı Giriniz: ")
parola = input("Parola Giriniz: ")

if sys_Kullanici_adi == Kullanici_adi and sys_parola != parola:
    print ("Parola Hatalı...")

elif sys_Kullanici_adi != Kullanici_adi and sys_parola == parola:
    print("Kullanıcı Adı Hatalı...")

elif sys_Kullanici_adi != Kullanici_adi and sys_parola != parola:
    print("Kullanıcı Adı ve Parola Hatalı")

else:
    print("Sisteme Başarıyla Giriş Yapıldı...")