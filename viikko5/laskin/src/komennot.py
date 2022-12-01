class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.edellinen_tila = 0

    def suorita(self):
        self.edellinen_tila = self.sovelluslogiikka.tulos
        syote = self.lue_syote()
        self.sovelluslogiikka.plus(int(syote))

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_tila)


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.edellinen_tila = 0

    def suorita(self):
        self.edellinen_tila = self.sovelluslogiikka.tulos
        syote = self.lue_syote()
        self.sovelluslogiikka.miinus(int(syote))

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_tila)


class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.edellinen_tila = 0

    def suorita(self):
        self.edellinen_tila = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa()

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_tila)


class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        pass
