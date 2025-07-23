"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.

Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

*İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*
"""
toplam = 0;
while True:
    sayı = input("Eklemek İstediğiniz Sayıyı Giriniz(Çıkmak için 'q'ya basınız.): ")
    if sayı.lower() == "q":
        print("Son Toplam Değeri: {}".format(toplam))
        print("Programdan Çıkılıyor...")
        break


    else:
        sayı = int(sayı)
        eski_toplam = toplam
        print("Eski Toplam: {}\t|\tGirdiğiniz Sayı: {}\n".format(toplam,sayı))
        toplam += sayı
        print("Eski Toplam : {} + {} = {}\n".format(eski_toplam ,sayı, toplam))
        print("Güncel Toplam Değeri: {}\n".format(toplam))


