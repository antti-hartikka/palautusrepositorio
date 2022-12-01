KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, joukon_kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(joukon_kapasiteetti, int) or joukon_kapasiteetti < 0:
            raise Exception("Kapasiteetti ei ole positiivinen kokonaisluku")
        else:
            self.kapasiteetti = joukon_kapasiteetti

        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._alusta_taulukko(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu_joukkoon(self, luku):
        return luku in self.lukujono

    def lisaa_joukkoon(self, luku):
        if not self.kuuluu_joukkoon(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm == len(self.lukujono):
                self._kasvata_taulukkoa()

    def poista(self, luku):
        if luku in self.lukujono:
            indeksi = self.lukujono.index(luku)
            self.lukujono[indeksi] = 0

            for j in range(indeksi, self.alkioiden_lkm - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def _kasvata_taulukkoa(self):
        taulukko_old = self.lukujono
        self.kopioi_taulukko(self.lukujono, taulukko_old)
        self.lukujono = self._alusta_taulukko(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._alusta_taulukko(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def _alusta_taulukko(koko):
        return [0] * koko

    def lisaa_kaikki_joukkoon(self, taulu):
        for luku in taulu:
            self.lisaa_joukkoon(luku)

    @staticmethod
    def yhdiste(a_joukko, b_joukko):
        yhdistejoukko = IntJoukko()

        yhdistejoukko.lisaa_kaikki_joukkoon(a_joukko.to_int_list())
        yhdistejoukko.lisaa_kaikki_joukkoon(b_joukko.to_int_list())

        return yhdistejoukko

    @staticmethod
    def leikkaus(a_joukko, b_joukko):
        leikkausjoukko = IntJoukko()
        a_taulu = a_joukko.to_int_list()

        for luku in a_taulu:
            if b_joukko.kuuluu_joukkoon(luku):
                leikkausjoukko.lisaa_joukkoon(luku)

        return leikkausjoukko

    @staticmethod
    def erotus(a_joukko, b_joukko):
        erotusjoukko = IntJoukko()
        a_taulu = a_joukko.to_int_list()
        b_taulu = b_joukko.to_int_list()

        erotusjoukko.lisaa_kaikki_joukkoon(a_taulu)

        for luku in b_taulu:
            erotusjoukko.poista(luku)

        return erotusjoukko

    def __str__(self):
        return "{" + ", ".join(map(lambda luku: str(luku), self.to_int_list())) + "}"
