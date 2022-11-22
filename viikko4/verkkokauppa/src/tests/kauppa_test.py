import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = lambda t: [10, 10, 0][t-1]
        self.varasto_mock.hae_tuote.side_effect = lambda t: Tuote(t, ["maito", "limpsa", "olut"][t-1], [3, 5, 7][t-1])
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kaupan_tilimaksu_toimii_oikein_kaupan_paatteeksi(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("hannu", "234567")

        self.pankki_mock.tilisiirto.assert_called_with("hannu", 42, "234567", "33333-44455", 3)

    def test_asiointi_toimii_kahden_eri_tuotteen_kanssa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "45676666", "33333-44455", 8)

    def test_asiointi_toimii_kahden_saman_tuotteen_kanssa(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "45676666", "33333-44455", 6)

    def test_asiointi_toimii_kun_yksi_tuote_on_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "45676666", "33333-44455", 3)

    def test_asiointi_alkaa_puhtaalta_poydalta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("hannu", "123456")

        self.pankki_mock.tilisiirto.assert_called_with("hannu", 42, "123456", "33333-44455", 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksulle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("hannu", "123456")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_tuotteen_poisto_ostoskorista_toimii(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "45676666")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "45676666", "33333-44455", 6)
