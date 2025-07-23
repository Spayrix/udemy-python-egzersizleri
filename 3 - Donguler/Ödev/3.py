"""
1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
"""

print("1'den 10'a Kadar Olan Çarpım Tablosu Aşağıda Yazılmıştır.")


for i in range(1,11):
    for j in range(1,11):
            print("{} x {} = {}".format(j,i,j*i),end="\t\t")
    print()
