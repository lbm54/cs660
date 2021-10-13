def miniMax(self, state):
    
    if self.terminal():
        return self.utility(MAX)

    elif self.player == MAX:
        acts = self.actions()
        max = float("-inf")
        for a in acts:
            val = miniMax(self.Results(a, state))
            if val > max:
                max = val
        return max

    else:
        acts = self.actions()
        min = float("inf")
        for a in acts:
            val = miniMax(self.Results(a, self.state))
            if val < min:
                min = val
        return min
