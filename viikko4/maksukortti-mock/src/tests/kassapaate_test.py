import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti_mock = Mock()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        self.maksukortti_mock.saldo = 10
        self.kassa.osta_lounas(self.maksukortti_mock)
        self.maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        self.maksukortti_mock.saldo = 4
        self.assertEqual(self.maksukortti_mock.saldo, 4)
        self.kassa.osta_lounas(self.maksukortti_mock)
        self.maksukortti_mock.osta.assert_not_called()

    def test_kortille_ladataan_rahaa(self):
        self.kassa.lataa(self.maksukortti_mock, 10)
        self.maksukortti_mock.lataa.assert_called_with(10)

    def test_kortille_ei_ladata_negatiivista_summaa(self):
        self.kassa.lataa(self.maksukortti_mock, -10)
        self.maksukortti_mock.lataa.assert_not_called()
