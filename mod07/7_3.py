def gallon(num):
    g = num * 3.785
    return g
num = int(input("Syötä gallonmäärä: "))
while num >= 0:
    print(f"{num} gallonaa = {gallon(num)} litraa")
    num = int(input("Syötä seuraava gallonmäärä: "))

#while True