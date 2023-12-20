from kps_default import KiviPaperiSakset


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = KiviPaperiSakset()
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        if peli := peli.vaihda_peli_muotoa(vastaus):
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
