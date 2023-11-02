import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy


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

    def test_top_points(self):
        all = self.stats.top(5, SortBy.POINTS)
        self.assertEqual(len(self.stats.top(1, SortBy.POINTS)), 1)
        self.assertEqual(len(all), 5)
        self.assertRaises(IndexError, self.stats.top, 6, SortBy.POINTS)
        corr = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]

        for i in range(5):
            self.assertEqual(all[i].name, corr[i])

    def test_top_assists(self):
        all = self.stats.top(5, SortBy.ASSISTS)
        self.assertEqual(len(self.stats.top(1, SortBy.ASSISTS)), 1)
        self.assertEqual(len(all), 5)
        self.assertRaises(IndexError, self.stats.top, 6, SortBy.ASSISTS)
        corr = ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"]

        for i in range(5):
            self.assertEqual(all[i].name, corr[i])

    def test_top_goals(self):
        all = self.stats.top(5, SortBy.GOALS)
        self.assertEqual(len(self.stats.top(1, SortBy.GOALS)), 1)
        self.assertEqual(len(all), 5)
        self.assertRaises(IndexError, self.stats.top,6, SortBy.GOALS)
        corr = ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"]

        for i in range(5):
            self.assertEqual(all[i].name, corr[i])

    def test_faulty_sort(self):
            self.assertIsNone(self.stats.top(5, "Faulty argument"))
