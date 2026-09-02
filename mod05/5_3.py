pienin = None
suurin = None
while True:
    syöte = input("Anna luku (tyhjä lopettaa): ")
    if syöte == "":
        break
    luku = int(syöte)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
print("Pienin luku on", pienin)
print("Suurin luku on", suurin)