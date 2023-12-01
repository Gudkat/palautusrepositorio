KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not self._is_valid(kapasiteetti) or not self._is_valid(kasvatuskoko):
            raise Exception(
                "Kapasiteetin ja kavatuskoon pitää olla vähintään 0 ja tyyppiä int")
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.lukujono[:self.alkioiden_lkm]:
            return True
        return False

    def lisaa(self, luku: int):
        if self.kuuluu(luku):
            return False

        if self.alkioiden_lkm == len(self.lukujono):
            uusi_taulukko = self._luo_lista(
                self.alkioiden_lkm + self.kasvatuskoko)
            for indexi, arvo in enumerate(self.lukujono):
                uusi_taulukko[indexi] = arvo
            self.lukujono = uusi_taulukko
        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True

    def poista(self, luku):
        try:
            kohta = self.lukujono.index(luku)
        except ValueError:
            return False

        self.lukujono[kohta] = 0
        for i in range(kohta, self.alkioiden_lkm - 1):
            self.lukujono[i] = self.lukujono[i + 1]
        self.lukujono[-1] = 0
        self.alkioiden_lkm -= 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def get_min_size_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(len(taulu)):
            taulu[i] = self.lukujono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.get_min_size_list()
        b_taulu = b.get_min_size_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(joukko1, joukko2):
        uusi_joukko = IntJoukko()
        lista_1 = joukko1.get_min_size_list()
        lista_2 = joukko2.get_min_size_list()

        for alkio in lista_1:
            if alkio in lista_2:
                uusi_joukko.lisaa(alkio)

        return uusi_joukko

    @staticmethod
    def erotus(joukko1, joukko2):
        uusi_joukko = IntJoukko()
        lista_1 = joukko1.get_min_size_list()
        lista_2 = joukko2.get_min_size_list()

        for alkio in lista_1:
            if alkio not in lista_2:
                uusi_joukko.lisaa(alkio)

        return uusi_joukko

    def __str__(self):
        return "{" + ", ".join([str(luku) for luku in self.get_min_size_list()]) + "}"

    def _is_valid(self, luku):
        return isinstance(luku, int) and luku >= 0
