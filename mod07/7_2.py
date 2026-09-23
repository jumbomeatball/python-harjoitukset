import random
def noppa(max):
    num = random.randint(1, max)
    return num
heitto = 1
arvo = 0
max= int(input("Syötä näärä:"))
while arvo != max:
    arvo = noppa(max)
    print(f"Heitto {heitto}: {arvo}")
    heitto = heitto + 1