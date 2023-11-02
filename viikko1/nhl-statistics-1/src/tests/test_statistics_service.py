import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stats = StatisticsService(
            PlayerReaderStub())
        
    def test_creating_constructor(self):
        self.assertTrue(self.stats)
        self.assertTrue(self.stats._players)

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")
        self.assertEqual(type(self.stats.search("Semenko")), Player)
        self.assertEqual(len(self.stats._players), 5)
        self.assertTrue(self.stats.search("Gretzky"))
        self.assertIsNone(self.stats.search("Matti Luukkainen"))

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("PIT")), 1)
        self.assertEqual(len(self.stats.team("DET")), 1)
        self.assertEqual(len(self.stats.team("PHI")), 0)
        self.assertEqual(self.stats.team("DET")[0].name, "Yzerman")

    def test_top(self):
        self.assertEqual(len(self.stats.top(1)), 1)
        self.assertEqual(len(self.stats.top(2)), 2)
        self.assertEqual(len(self.stats.top(3)), 3)
        self.assertEqual(len(self.stats.top(4)), 4)
        self.assertEqual(len(self.stats.top(5)), 5)
        self.assertRaises(IndexError, self.stats.top, 6)
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")
        self.assertEqual(self.stats.top(2)[1].name, "Lemieux")
        self.assertEqual(self.stats.top(3)[2].name, "Yzerman")
        self.assertEqual(self.stats.top(4)[3].name, "Kurri")
        self.assertEqual(self.stats.top(5)[4].name, "Semenko")

