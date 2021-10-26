from reversiboard import RBoard
from ai.strategies import Strategies

def minimax(state, alpha, beta, depth, maximizingPlayer, index):
    #state = RBoard(state)

    if state.terminal(): 
        return (state.utility(state.player()), None)
    elif depth == 0:
        strategy = Strategies()
        return (strategy.heuristic(index, state), None)

    if maximizingPlayer:
        max_val = (float("-inf"), None)
        for act in state.actions():
            val = minimax(state.result(act), alpha, beta, depth - 1, False, act)
            if (val[0] > max_val[0]): 
                max_val = (val[0], act)
            alpha = max(val[0], alpha)
            #minimizing player had a better option somewhere else in the tree, so prune
            if beta <= alpha: break
        return max_val
    else:
        min_val = (float("inf"), None)
        for act in state.actions():
            val = minimax(state.result(act), alpha, beta, depth - 1, True, act)
            if (val[0] < min_val[0]):
                min_val = (val[0], act)
            beta = min(val[0], beta)
            #maximizing player had a better option, so prune
            if beta <= alpha: break
        return min_val