# from reversiBoardGroup4 import RBoardGroup4

class Strategies():

    def heuristic(self, index, board):
        val = self.cornersCaptured(index, board)
        val2 = self.countPieces(board)
        # self.someotherstrategy
        # return max(val1, val2, val3)
        return max(val, val2)

    # def __init__(self, board):
    #     val2 = self.countPieces(board)
    #     # self.someotherstrategy
    #     # return max(val1, val2, val3)
    #     return val2

        #FIXME -- mobility and stability
#     def mobility(self, board):
#         if (board.actions() + Min Player Moves != 0)
# 	Mobility Heuristic Value =
# 		100 * (Max Player Moves - Min Player Moves) / (Max Player Moves + Min Player Moves)
# else
# 	Mobility Heuristic Value = 0

# https://github.com/arminkz/Reversi/blob/master/src/game/BoardHelper.java

    def countPieces(self, board):
        return board.countpieces(board.player()) - board.countpieces(board.otherplayer())

    def cornersCaptured(self, index, board):
        list = [(0, 0), (7, 0), (0, 7), (7, 7)]
        retVal = 0
       
        if index in list:
            maxPlayer = board.player()
            minPlayer = board.otherplayer()
            maxPlayerCorners = 0 
            minPlayerCorners = 0
            for listIndex in list:
                if board.data[listIndex[0]][listIndex[1]] == maxPlayer: maxPlayerCorners += 1
                if board.data[listIndex[0]][listIndex[1]] == minPlayer: minPlayerCorners += 1
            if (maxPlayerCorners + minPlayerCorners != 0):
                retVal = 100 * (maxPlayerCorners - minPlayerCorners) / (maxPlayerCorners + minPlayerCorners)
        return retVal


    # def killerMove():
    #     pass
        #does this win

    # another strategy

#     Corner Grab (Measures if the current player can take a corner with its next move, Weighted highly at all times.)

# Stability (Measures the number of discs that cannot be flipped for the rest of the game. Weighted highly at all times.)

# Mobility (Measures the number of moves the player is currently able to make. Has significant weight in the opening game, but diminishes to zero weight towards the endgame.)

# Placment (piece placement score of the current player minus the piece placement score of the opponent.)

# Frontier Discs (number of spaces adjacent to opponent pieces minus the the number of spaces adjacent to the current player's pieces.)

# Disc difference (Measures the difference in the number of discs on the board. Has zero weight in the opening, but increases to a moderate weight in the midgame, and to a significant weight in the endgame.)

# Parity (Measures who is expected to make the last move of the game. Has zero weight in the opening, but increases to a very large weight in the midgame and endgame.) (currently unused feature)

# Killer Move Detection
# The AI Player takes some moves without searching within the Minimax tree:

# Corner Grab Move (Move that leads to capturing a corner)

# Blocking Move (Move that blocks the oponent on the next move)