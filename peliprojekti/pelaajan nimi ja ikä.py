print("Kerro pelaajan nimi:")
name = input()
print("Kerro ikäsi:")
age = input()
print(f"Pelaajan nimi: {name}")
print(f"Ikä: {age}")


if int(age) < 12:
    print("Pelaaja on alaikäinen. Pelaaminen ei ole sallittua! Ohjelma sammuu. . .")
else: 
    print("Tervetuloa peliin, " + name + "!")


print("✢ PÄÄVALIKKO ✢")
print("✦ 1. Pelaa peliä")
print("✦ 2. Näytä pelaajan tiedot")
print("✦ 3. Asetukset")
print("✦ 4. Ohjeet")
print("✦ 5. Lopeta peli")
syöte = int(input("Valitse vaihtoehto (1-5): "))

while syöte != "5":
    print("✢ PÄÄVALIKKO ✢")
    print("✦ 1. Pelaa peliä")
    print("✦ 2. Näytä pelaajan tiedot")
    print("✦ 3. Asetukset")
    print("✦ 4. Ohjeet")
    print("✦ 5. Lopeta peli")
    syöte = input("Valitse vaihtoehto (1-5): ")
    if syöte == "1":
        print("Peli alkaa!")
    elif syöte == "2":
        print(f"Pelaajan nimi: {name}")
        print(f"Ikä: {age}")
    elif syöte == "3":
        print("Asetukset-valikko")
    elif syöte == "4":
        print("Ohjeet-valikko")
    elif syöte == "5":
        print("Peli lopetetaan. Kiitos pelaamisesta!") 

    if syöte == "lopeta":
        break