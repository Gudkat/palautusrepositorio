class Komentotehdas:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.komennot = {
            "summa": Summa,
            "erotus": Erotus,
            "nollaus": Nollaus,
            "kumoa": Kumoa
        }

    def suorita(self, komento, arvo=0):
        operaatio = self.komennot[komento]
        return operaatio(self.sovelluslogiikka, arvo)


class Summa:
    def __init__(self, sovelluslogiikka, luku):
        sovelluslogiikka.plus(luku)


class Erotus:
    def __init__(self, sovelluslogiikka, luku):
        sovelluslogiikka.miinus(luku)


class Nollaus:
    def __init__(self, sovelluslogiikka, luku=0):
        sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka, luku=0):
        if len(sovelluslogiikka.historia) == 0:
            return
        sovelluslogiikka.kumoa()
