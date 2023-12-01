class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.historia = []

    def miinus(self, operandi):
        self.tallenna()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.tallenna()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.tallenna()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        self.aseta_arvo(self.historia.pop())

    def tallenna(self):
        self.historia.append(self._arvo)
