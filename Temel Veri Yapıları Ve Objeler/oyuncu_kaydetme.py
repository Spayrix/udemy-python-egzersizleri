print("Oyuncu Kaydetme Program")
print("---------------------------")

ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takım = input("Oyuncunun Takımı: ")

bilgiler = [ad,soyad,takım]

print("")
print("Bilgiler Kaydediliyor...")
print("")

print ("Oyuncu Adı: {}\nOyuncu Soyadı: {}\nOyuncunun Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi...")
