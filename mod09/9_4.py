import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus = 0
        self.kuljettu_matka = kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + muutos    
        if uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            uusi_nopeus = 0
        self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit

#pääohjelma
autot = []
for i in range(11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_käynnissä = True
while kilpailu_käynnissä:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_käynnissä = False
            break

print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nykyinen nopeus':<18}{'Kuljettu matka':<15}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}{auto.tämänhetkinen_nopeus:<18}{auto.kuljettu_matka:<15}")
print( )

auto = Auto("ABC-123", 142, 0, 0)
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", str(auto.huippunopeus) + "km/h")
print("Tämänhetkinen nopeus:", str(auto.tämänhetkinen_nopeus) + "km/h")
print("Kuljettu matka:", str(auto.kuljettu_matka) + "km/h")

print( )

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Nopeus kiihdytyksen jälkeen:", str(auto.tämänhetkinen_nopeus) + "km/h")

auto.kiihdytä(-200)
print("Nopeus hätäjarrutuksen jälkeen:", str(auto.tämänhetkinen_nopeus) + "km/h")