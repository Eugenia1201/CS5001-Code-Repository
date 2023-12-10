""" Rock Paper Scissors Game
"""

import enum


class RPS(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def rock_paper_scissors(player1, player2):
    if player1 == player2:
        result = "Tie!"
    elif (player1 == RPS.ROCK) and (player2 == RPS.PAPER):
        result = "Player 2 wins!"
    elif (player1 == RPS.PAPER) and (player2 == RPS.SCISSORS):
        result = "Player 2 wins!"
    elif (player1 == RPS.SCISSORS) and (player2 == RPS.ROCK):
        result = "Player 2 wins!"
    else:
        result = "Player 1 wins!"
    return result
