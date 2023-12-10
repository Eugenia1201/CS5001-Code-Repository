""" Test Rock Paper Scissors
"""

import unittest
import rockpaperscissors as rps


class TestRockPaperScissors(unittest.TestCase):
    def test_player_2_wins(self):
        self.assertEqual(rps.rock_paper_scissors(rps.RPS.ROCK, rps.RPS.PAPER),
                         "Player 2 wins!")


if __name__ == "__main__":
    unittest.main()
