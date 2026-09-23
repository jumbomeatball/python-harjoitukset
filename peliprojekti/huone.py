class Huone:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.esineet = []

    def lisaa_esine(self, esine):
        self.esineet.append(esine)

    def poista_esine(self, esine):
        if esine in self.esineet:
            self.esineet.remove(esine)