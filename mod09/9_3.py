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