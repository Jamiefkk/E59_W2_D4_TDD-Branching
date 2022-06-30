import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def test_get_result_home_win(self):
        result = {"home_score": 1, "away_score": 0}
        self.assertEqual("Home win", self.football_results.get_result(result))

    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
