"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""
""" 
def sayı_okunus():
    sayi = int(input("2 basamaklı bir sayı girin: "))
    onlar = sayi // 10
    birler = sayi % 10

    onlar_dict = {1: "On", 2: "Yirmi", 3: "Otuz", 4: "Kırk", 5: "Elli",
        6: "Altmış", 7: "Yetmiş", 8: "Seksen", 9: "Doksan"
    }

    birler_dict = {
        1: "Bir", 2: "İki", 3: "Üç", 4: "Dört", 5: "Beş",
        6: "Altı", 7: "Yedi", 8: "Sekiz", 9: "Dokuz"
    }
    okunus = onlar_dict[onlar]
    if birler != 0:
        okunus += " " + birler_dict[birler]

    print(f"{sayi}: {okunus}")

sayı_okunus()
"""
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))

print(okunus(sayı))