class Hissi:
    def __init__(self, alin, ylin):
            self.alin = alin
            self.ylin = ylin
            self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
         if self.kerros < self.ylin:
             self.kerros += 1
             print("Hissi on kerroksessa:", self.kerros)

    def kerros_alas(self):
         if self.kerros > self.alin:
             self.kerros -= 1
             print("Hissi on kerroksessa:", self.kerros)

class Talo:
    def __init__(self, alin, ylin, hissien_määrä):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissillä(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

def palohälytys(self):
    for hissi in self.hissit:
        hissi.siirry_kerrokseen(self.alin)

talo = Talo(1, 10, 3)

talo.aja_hissillä(1, 8)
talo.aja_hissillä(2, 5)
talo.aja_hissillä(3, 10)

print("PALOHÄLYTYS!!!")

talo.palohälytys()