import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            uusi_nopeus = 0
        self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autolista):
        self.nimi = nimi
        self.pituus = kilometrimäärä
        self.autot = autolista

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nykyinen nopeus':<18}{'Kuljettu matka':<15}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}{auto.tämänhetkinen_nopeus:<18}{auto.kuljettu_matka:<15}")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False



autot = []
for i in range(10):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja += 1
    if tunteja % 10 == 0:
        print(f"--- {tunteja} tuntia kulunut ---")
        kilpailu.tulosta_tilanne()

print(f"=== Kilpailu {kilpailu.nimi} on ohi {tunteja} tunnin jälkeen ===")
kilpailu.tulosta_tilanne()