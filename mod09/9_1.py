class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus = 0
        self.kuljettu_matka = kuljettu_matka = 0

auto = Auto("ABC-123", 142, 0, 0)
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", str(auto.huippunopeus) + "km/h")
print("Tämänhetkinen nopeus:", str(auto.tämänhetkinen_nopeus) + "km/h")
print("Kuljettu matka:", str(auto.kuljettu_matka) + "km/h")