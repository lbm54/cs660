class Strategy():
    def isCornerPiece(index):
        return index in [(0,0), (63, 63), (63, 0), (0, 63)]

    def killerMove():
        pass
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