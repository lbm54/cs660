from reversiboard import RBoard

class minimax():
    def minimax(self, state, alpha, beta, depth, maximizingPlayer):
        if depth == 0 or state.terminal(): 
            ### check this
            return RBoard.utility(state.player())
        if maximizingPlayer:
            max_val = float("-inf")
            for act in state.actions():
                val = self.minimax(state.result(act), alpha, beta, depth - 1, False)
                max_val = max(val, max_val)
                alpha = max(val, alpha)
                #minimizing player had a better option somewhere else in the tree, so prune
                if beta <= alpha: break
            return max_val
        else:
            min_val = float("inf")
            for act in state.actions():
                val = self.minimax(state.result(act), alpha, beta, depth - 1, True)
                min_val = min(val, min_val)
                beta = min(val, beta)
                #maximizing player had a better option, so prune
                if beta <= alpha: break
            return min_val