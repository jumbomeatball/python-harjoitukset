luvut = []

while True:
    syöte = input("Syötä luku: (tyhjä lopettaa) ")
    if syöte == "":
        break
    luvut.append(int(syöte))

luvut.sort(reverse=True)

print("Viisi suurinta lukua: ")
for luku in luvut[:5]:
    print(luku)