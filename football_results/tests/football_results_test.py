import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def test_get_result_home_win(self):
        result = {"home_score": 1, "away_score": 0}
        self.assertEqual("Home win", get_result(result))

    def test_get_result_draw(self):
        result = {"home_score": 100, "away_score": 100}
        self.assertEqual("Draw", get_result(result))

    def test_get_result_away_win(self):
        result = {"home_score": 0, "away_score": 3}
        self.assertEqual("Away win", get_result(result))

    def test_list_of_results(self):
        game1 = {"home_score": 1, "away_score": 0}
        game2 = {"home_score": 0, "away_score": 3}
        game3 = {"home_score": 100, "away_score": 100}
        results = [game1, game2, game3]
        self.assertEqual(["Home win", "Away win", "Draw"], get_results(results))

    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 