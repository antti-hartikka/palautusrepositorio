import unittest
from statistics import Statistics, SortBy
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


class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_finds_player(self):
        result = self.statistics.search("Gretzky")
        self.assertEqual(result.name, "Gretzky")

    def test_search_does_not_find(self):
        result = self.statistics.search("Gretzkyy")
        self.assertEqual(result, None)

    def test_team_search_works(self):
        result = self.statistics.team("EDM")
        self.assertEqual(result[0].name, "Semenko")
        self.assertEqual(result[1].name, "Kurri")
        self.assertEqual(result[2].name, "Gretzky")

    def test_empty_list_team(self):
        result = self.statistics.team("EMD")
        self.assertEqual(len(result), 0)

    def test_top_players_default(self):
        result = self.statistics.top(4)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_players_points(self):
        result = self.statistics.top(4, SortBy.POINTS)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].name, "Gretzky")

    def test_top_players_goals(self):
        result = self.statistics.top(4, SortBy.GOALS)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].name, "Lemieux")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Kurri")

    def test_top_players_assists(self):
        result = self.statistics.top(4, SortBy.ASSISTS)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Lemieux")


if __name__ == '__main__':
    unittest.main()
