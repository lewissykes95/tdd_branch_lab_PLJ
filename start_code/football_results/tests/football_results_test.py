import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):


    def setUp(self):
        self.football_results1 = {    
                "home_score": 0,
                "away_score": 1
                }   
        self.football_results2 = {    
                "home_score": 1,
                "away_score": 0
                }   
        self.football_results3 = {    
                "home_score": 1,
                "away_score": 1
                }   
    
    def test_get_right_result(self):
        result = get_result(self.football_results1)
        self.assertEqual("away win", result)

    def test_get_right_result2(self):
        result = get_result(self.football_results2)
        self.assertEqual("home win", result)

    def test_get_right_result3(self):
        result = get_result(self.football_results3)
        self.assertEqual("draw", result)
    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 

# if __name__ == "__main__":
#     unittest.main()




