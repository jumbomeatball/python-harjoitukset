import random

luku = random.randint(1, 10)
arvaus = 0

while arvaus != luku:
    arvaus = int(input("Arvaa luku: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")