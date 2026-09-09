print("Kerro pelaajan nimi:")
name = input()
print("Kerro ikäsi:")
age = input()
print(f"Pelaajan nimi: {name}")
print(f"Ikä: {age}")

lista = []


def pelaa_peli():
    print("Peli alkaa!")


def nayta_tiedot():
    print(f"Pelaajan nimi: {name}")
    print(f"Ikä: {age}")


def lisaa_esine():
    esineet = input("Anna esine: ")
    lista.append(esineet)


def nayta_esineet():
    print("Esineet:")
    for esine in lista:
        print(esine)


def aseta_asetukset():
    print("Asetukset-valikko")


def nayta_ohjeet():
    print("Ohjeet-valikko")


if int(age) < 12:
    print("Pelaaja on alaikäinen. Pelaaminen ei ole sallittua! Ohjelma sammuu. . .")
else: 
    print("Tervetuloa peliin, " + name + "!")

    print("✢ PÄÄVALIKKO ✢")
    print("✦ 1. Pelaa peliä")
    print("✦ 2. Näytä pelaajan tiedot")
    print("✦ 3. Lisää esine")
    print("✦ 4. Näytä esineet")
    print("✦ 5. Asetukset")
    print("✦ 6. Ohjeet")
    print("✦ 7. Lopeta peli")
    syöte = input("Valitse vaihtoehto (1-7): ")

    while syöte != "7":
        print("✢ PÄÄVALIKKO ✢")
        print("✦ 1. Pelaa peliä")
        print("✦ 2. Näytä pelaajan tiedot")
        print("✦ 3. Lisää esine")
        print("✦ 4. Näytä esineet")
        print("✦ 5. Asetukset")
        print("✦ 6. Ohjeet")
        print("✦ 7. Lopeta peli")
        syöte = input("Valitse vaihtoehto (1-7): ")

        if syöte == "1":
            pelaa_peli()
        elif syöte == "2":
            nayta_tiedot()
        elif syöte == "3":
            lisaa_esine()
        elif syöte == "4":
            nayta_esineet()
        elif syöte == "5":
            aseta_asetukset()
        elif syöte == "6":
            nayta_ohjeet()
        elif syöte == "7":
            print("Peli lopetetaan. Kiitos pelaamisesta!")