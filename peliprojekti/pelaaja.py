class Pelaaja:
    def __init__(self, nimi, aloitus_huone):
        self.nimi = nimi
        self.sijainti = aloitus_huone
        self.esineet = [] 


    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone
        print(f"Liikuit huoneeseen: {self.sijainti.nimi}")

    def keraa_esine(self):
        if self.sijainti.esineet:
            keratty = self.sijainti.esineet[0]
            self.sijainti.poista_esine(keratty)
            self.esineet.append(keratty)
            print(f"Keräsit esineen: {keratty.nimi}")
        else:
            print("Huoneessa ei ole esineitä.")