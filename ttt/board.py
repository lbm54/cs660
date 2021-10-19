class Board():

    def __init__(self):
        self.currentState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def terminal(self, state = None):
        if state is None: state = self.currentState
        cases = {}
        cases[0] = state[0][0] + state[0][1] + state[0][2]
        cases[1] = state[1][0] + state[1][1] + state[1][2]
        cases[2] = state[2][0] + state[2][1] + state[2][2]
        cases[3] = state[0][0] + state[1][0] + state[2][0]
        cases[4] = state[0][1] + state[1][1] + state[2][1]
        cases[5] = state[0][2] + state[1][2] + state[2][2]
        cases[6] = state[0][0] + state[1][1] + state[2][2]
        cases[7] = state[2][0] + state[1][1] + state[0][2]

        for i in range(0, 8): 
            if cases[i] == 3:
                return 1
            if cases[i] == -3:
                return -1

        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0: return None
        else: 
            return 0

    def actions(self, state):
        retVal = []
        for indexI in range(0, 3):
            for indexJ in range(0, 3):
                if state[indexI][indexJ] == 0: retVal.append((indexI, indexJ))
        return retVal

    def results(self, state, action, maximizingPlayer):
        state[action[0]][action[1]] = 1 if maximizingPlayer else -1
        return state

    def minimax(self, state, alpha, beta, maximizingPlayer):
        result = self.terminal(state)
        if result is not None: return (result, None)
        if maximizingPlayer:
            max_val = (float("-inf"), None)
            for act in self.actions(state):
                val = self.minimax(self.results(state, act, maximizingPlayer), alpha, beta, False)
                if (val[0] > max_val[0]): 
                    max_val = (val[0], act)
                alpha = max(val[0], alpha)
                state[act[0]][act[1]] = 0
                #minimizing player had a better option somewhere else in the tree, so prune
                if beta <= alpha: break
            return max_val
        else:
            min_val = (float("inf"), None)
            for act in self.actions(state):
                val = self.minimax(self.results(state, act, maximizingPlayer), alpha, beta, True)
                if (val[0] < min_val[0]): 
                    min_val = (val[0], act)
                beta = min(val[0], beta)
                state[act[0]][act[1]] = 0
                #maximizing player had a better option, so prune
                if beta <= alpha: break
            return min_val