MAX = 0
MIN = 0
class miniMax():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    youreFirst = None
    yourTurn = False
    def terminal():
        # if game is over regardless of win
            return 0
    def utility(state):
        # if somenone won
        return 0
    def actions(self):
        retVal = []
        for i in range (len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is 0:
                    retVal.append((i,j))
        return retVal
    def player():
        # determine who next player is.
        return 0
    def results(state, actions):
        # next board based on state and possible action
        return 0
    def miniMax(self, state):
        if self.terminal():
            return self.utility(MAX)
        elif self.player == MAX:
            acts = self.actions()
            max = float("-inf")
            for a in acts:
                val = self.miniMax(self.results(a, state))
                if val > max:
                    max = val
            return max
        else:
            acts = self.actions()
            min = float("inf")
            for a in acts:
                val = self.miniMax(self.results(a, state))
                if val < min:
                    min = val
            return min
miniMax()