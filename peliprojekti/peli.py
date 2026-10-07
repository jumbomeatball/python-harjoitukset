from esine import Esine
from huone import Huone
from pelaaja import Pelaaja

#tallennus...
tallennustiedosto = "tallennus.txt"

def lue_tiedosto(polku):
        with open(polku, "r") as tiedosto:
            return tiedosto.read()

def tallenna_peli(pelaaja):
    with open(tallennustiedosto, "w") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(pelaaja.sijainti.nimi.lower() + "\n")
        for esine in pelaaja.esineet:
            tiedosto.write(esine.nimi + "\n")
    print("Peli tallennettu")
#tallennus...
 
#huoneet ja esineet
makuuhuone = Huone("Makuuhuone")
keittio = Huone("Keittiö")
olohuone = Huone("Olohuone")
eteinen = Huone("Eteinen")
wc = Huone("WC")
 
def luo_esineet():
    olohuone.lisaa_esine(Esine("Pizza", 0.4))
    olohuone.lisaa_esine(Esine("Keksi", 0.2))
    keittio.lisaa_esine(Esine("Suomalainen korvapuusti", 0.3))
    keittio.lisaa_esine(Esine("Banaani", 0.2))
    keittio.lisaa_esine(Esine("Suklaakakku", 0.3))
    makuuhuone.lisaa_esine(Esine("Karkkipussi", 0.3))
    eteinen.lisaa_esine(Esine("Omena", 0.2))
    wc.lisaa_esine(Esine("Ruisleipä", 0.1))
 
#ravintoarvot
ravintoarvot = {
    "Pizza": 5,
    "Suomalainen korvapuusti": 3,
    "Banaani": 2,
    "Suklaakakku": 2,
    "Karkkipussi": 1,
    "Keksi": 1,
    "Omena": 1,
    "Ruisleipä": 3,
}
 
#funktiot
def laske_ravinto(esine):
    if esine.nimi in ravintoarvot:
        return ravintoarvot[esine.nimi]
    return 0
 
def syo_esine(nalka):
    if len(pelaaja.esineet) == 0:
        print("Tyhjä. Nälkä kasvaa...")
        return nalka
 
    print("Mitä haluat syödä?")
    numero = 1
    for esine in pelaaja.esineet:
        print(f"{numero}. {esine}")
        numero = numero + 1
    valinta = input("Valitse numero: ")
 
    loytyi = False
    numero = 1
    for esine in pelaaja.esineet:
        if str(numero) == valinta:
            valittu = esine
            loytyi = True
        numero = numero + 1
 
    if loytyi == False:
        print("Virheellinen valinta.")
        return nalka
 
    pelaaja.esineet.remove(valittu)
    syodyt.append(valittu.nimi)
    nalka = nalka - laske_ravinto(valittu)
    if nalka < 0:
        nalka = 0
    print(f"Söit: {valittu.nimi}. Nälkää vielä: {nalka}")
    return nalka
 
def maaraa_loppu(syodyt):
    if "Pizza" in syodyt:
        return "1. reitti, voitit pelin syömällä vain yhden ruoan!"
    elif "Suomalainen korvapuusti" in syodyt:
        return "2. reitti, söit pelin aikana suomalaisen korvapuustin!"
    else:
        return "3. reitti, söit itsesi täyteen!"
 
def pelaa_peli(nalka):
    print("Peli alkaa!")
    jatka = True
    while jatka:
        print(f"Olet huoneessa: {pelaaja.sijainti.nimi}  (Nälkä: {nalka})")
        print("1. Liiku toiseen huoneeseen")
        print("2. Kerää esine")
        print("3. Syö esine")
        print("4. Takaisin päävalikkoon")
        valinta = input("Valitse (1-4): ")
 
        if valinta == "1":
            print("1. Makuuhuone")
            print("2. Keittiö")
            print("3. Olohuone")
            print("4. Eteinen")
            print("5. WC")
            kohde = input("Minne menet? ")
            if kohde == "1":
                pelaaja.liiku(makuuhuone)
            elif kohde == "2":
                pelaaja.liiku(keittio)
            elif kohde == "3":
                pelaaja.liiku(olohuone)
            elif kohde == "4":
                pelaaja.liiku(eteinen)
            elif kohde == "5":
                pelaaja.liiku(wc)
            else:
                print("Virheellinen valinta.")
        elif valinta == "2":
            pelaaja.keraa_esine()
        elif valinta == "3":
            nalka = syo_esine(nalka)
            if nalka == 0:
                jatka = False
        elif valinta == "4":
            jatka = False
        else:
            print("Virheellinen valinta.")
    return nalka
 
def nayta_tiedot(nalka):
    print(f"Pelaajan nimi: {name}")
    print(f"Ikä: {age}")
    print(f"Nälkä: {nalka}")
 
def lisaa_esine():
    esineet = input("Anna esine: ")
    pelaaja.esineet.append(Esine(esineet, 0.1))
 
def nayta_esineet():
    print("Esineet:")
    for esine in pelaaja.esineet:
        print(esine)
 
def aseta_asetukset():
    print("Asetukset-valikko")
 
def nayta_ohjeet():
    print(lue_tiedosto("ohjeet.txt"))
 
#🐱pääesikysymyset
def nayta_valikko():
    print("PÄÄVALIKKO")
    print("1. Pelaa peliä")
    print("2. Näytä pelaajan tiedot")
    print("3. Lisää esine")
    print("4. Näytä esineet")
    print("5. Asetukset")
    print("6. Ohjeet")
    print("7. Lopeta peli")
 
#pääohjelma
#intro.txt
print(lue_tiedosto("intro.txt"))
 
#esikysymykset
print("Kerro pelaajan nimi:")
name = input()
print("Kerro ikäsi:")
age = input()
print(f"Pelaajan nimi: {name}")
print(f"Ikä: {age}")
 
pelaaja = Pelaaja(name, eteinen)
nalka = 5
syodyt = []
luo_esineet()
 
if int(age) < 12:
    print("Pelaaja on alaikäinen. Pelaaminen ei ole sallittua! Ohjelma sammuu. . .")
else:
    print("Tervetuloa peliin, " + name + "!")
    nayta_valikko()
    syöte = input("Valitse vaihtoehto (1-7): ")
 
    while syöte != "7" and nalka > 0:
        if syöte == "1":
            nalka = pelaa_peli(nalka)
        elif syöte == "2":
            nayta_tiedot(nalka)
        elif syöte == "3":
            lisaa_esine()
        elif syöte == "4":
            nayta_esineet()
        elif syöte == "5":
            aseta_asetukset()
        elif syöte == "6":
            nayta_ohjeet()
        else:
            print("Virheellinen valinta.")
 
        if nalka > 0:
            nayta_valikko()
            syöte = input("Valitse vaihtoehto (1-7): ")
 
    if nalka == 0:
        print("Nam nam ei ole enää nälkä. Onneksi olkoon!")
        print(maaraa_loppu(syodyt))
    tallenna_peli(pelaaja)
    print("Peli lopetetaan. Kiitos pelaamisesta!")