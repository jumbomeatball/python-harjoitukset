nimi = str
lista = set()
while nimi != "":
    nimi = str(input("Anna nimi: "))
    if nimi in lista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        lista.add(nimi)