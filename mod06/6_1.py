import random

määrä = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(määrä):
    silmäluku = random.randint (1, 6)
    summa += silmäluku

print("Silmälukujen summa on:", summa)