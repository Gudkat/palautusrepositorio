from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly


class KiviPaperiSakset:
    def __init__(self, tuomari=None):
        if not tuomari:
            tuomari = Tuomari()
        self.tuomari = tuomari
        self.jatkuu = True

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)
        if self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        else:
            self.jatkuu = False

        print("Kiitos!")
        print(self.tuomari)
        if self.jatkuu:
            self.pelaa()

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ekan_siirto):
        # Vanha kunnon kivi ei petä koskaan
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto in ["k", "p", "s"]

    def vaihda_peli_muotoa(self, uusi_peli_muoto):
        if uusi_peli_muoto == "a":
            return self.luo_kaksinpeli(self.tuomari)
        elif uusi_peli_muoto == "b":
            return self.luo_tekoaly_peli(self.tuomari)
        elif uusi_peli_muoto == "c":
            return self.luo_parempi_tekoaly_peli(self.tuomari)
        return None

    @staticmethod
    def luo_kaksinpeli(tuomari):
        return luo_uusi_peli("a", tuomari)

    @staticmethod
    def luo_tekoaly_peli(tuomari):
        return luo_uusi_peli("b", tuomari)

    @staticmethod
    def luo_parempi_tekoaly_peli(tuomari):
        return luo_uusi_peli("c", tuomari)


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        if self.tekoaly:
            tokan_siirto = self.tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {tokan_siirto}")
            self.tekoaly.aseta_siirto(ekan_siirto)
            return tokan_siirto


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")


def luo_uusi_peli(uusi_peli_muoto, tuomari):
    if uusi_peli_muoto == "a":
        return KPSPelaajaVsPelaaja(tuomari)
    elif uusi_peli_muoto == "b":
        return KPSTekoaly(tuomari)
    elif uusi_peli_muoto == "c":
        return KPSParempiTekoaly(tuomari)
    return None

# Meni hermo circular importteihin ja muutenkin niin tungin ne kaikki tänne.
# Oispa ollu aikaa leikki enemmän ton kanssa. Jäi vähän scuffed :D
