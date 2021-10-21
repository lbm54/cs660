

from player import Player 
from ai.monte_carlo import MonteCarloTreeSearch

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p

    # TODO: update this function to use some effective combination of techniques discussed in class
    # Aim to take <5sec/move on reasonably modern hardware.
    # You should *always* beat the random player, and will score points for beating weak AIs as well.
    # To launch a game using this AI, run $ python3 play.py
    def taketurn(self, board):
        # board.print()

        # elf, state, alpha, beta, maximizingPlayer
        # return mm.minimax(board, float('-inf'), float('inf'), self.playerN, 5)
        
        # return random.sample(board.actions(),1)[0]

        MonteCarloTreeSearch(board, 1000)
    def player(self):
        return self.playerN
