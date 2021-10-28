

from player import Player 
from ai.monte_carlo import monteCarloTreeSearch
from ai.minimax import minimax, minimaxNoDepth
from datetime import datetime
from reversiboard import RBoard


class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
        self.turns = 0
        self.times = []

    # TODO: update this function to use some effective combination of techniques discussed in class
    # Aim to take <5sec/move on reasonably modern hardware.
    # You should *always* beat the random player, and will score points for beating weak AIs as well.
    # To launch a game using this AI, run $ python3 play.py
    def taketurn(self, board):
        if self.turns < 10:
            val = monteCarloTreeSearch(board, 1000 + self.turns * 40)
        elif self.turns < 21: 
            val = monteCarloTreeSearch(board, 1000 + self.turns * 60)
        elif self.turns < 23:
            val = minimax(board, float('-inf'), float('inf'), 8, False, None)[1]    
        elif self.turns < 25:
            val = minimax(board, float('-inf'), float('inf'), 9, False, None)[1]           
        else:
            val = minimaxNoDepth(board, float('-inf'), float('inf'), False)[1]
        self.turns += 1
        return val

    def player(self):
        return self.playerN
