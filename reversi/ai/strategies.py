# from reversiBoardGroup4 import RBoardGroup4

class Strategies():

    def heuristic(self, index, board):
        val = self.cornersCaptured(index, board)
        val2 = self.countPieces(board)
        return max(val, val2)

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

