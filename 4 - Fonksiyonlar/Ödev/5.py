"""
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
Pisagor üçlüsü, a2+b2=c2 eşitliğini sağlayan a, b,c tam sayılarına verilen addır.
"""

"""
def pisegor_bul():
    for a in range(1,101):
        for b in range(1,101):
            c_kare = a**2 + b**2
            c = c_kare ** 0.5
            if c < 100 and c % 1 == 0:
                print("a : ",a,"| b : ",b,"| c : ",int(c))

pisegor_bul()
"""


def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi


for i in pisagor_bulma():
    print(i)