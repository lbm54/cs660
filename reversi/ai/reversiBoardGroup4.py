
from reversiboard import RBoard

#out own board class that extends rboard
class RBoardGroup4(RBoard):

    #init should copy the board
    def __init__(self, rboard):
        self.data = []
        for r in range(8):
            self.data.append([])
            for c in range(8):
                self.data[r].append(rboard.data[r][c])
        self.nextplayer = rboard.nextplayer

    def validcapture(self, coord, d):
        n = 0
        rd,cd = d
        r,c = coord
        rcur = r + rd
        ccur = c + cd
        while 0 <= rcur < 8 and 0 <= ccur < 8 and self.data[rcur][ccur] == self.otherplayer():
            n += 1
            rcur += rd
            ccur += cd
        return n > 0 and 0 <= rcur < 8 and 0 <= ccur < 8 and self.data[rcur][ccur] == self.player()

    def validmove(self, coord):
        r,c = coord
        if self.data[r][c] != 0: return False
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for d in dirs:
            if self.validcapture(coord, d): return True
        return False

    def actions(self):
        # return a set of all valid moves
        coords = set()
        for r in range(8):
            for c in range(8):
                if self.validmove((r,c)):
                    coords.add((r,c))
        return frozenset(coords)

    def player(self):
        return self.nextplayer
    def otherplayer(self):
        if self.nextplayer == 1: return 2
        else: return 1

    def simResult(self, coord):
        #we won't check if it's valid
        # if self.validmove(coord):
        # nextboard = copy.deepcopy(self)
        r,c = coord
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for d in dirs:
            if self.validcapture(coord, d):
                rd,cd = d
                rcur = r + rd
                ccur = c + cd
                while 0 <= rcur < 8 and 0 <= ccur < 8 and self.data[rcur][ccur] == self.otherplayer():
                    self.data[rcur][ccur] = self.player()
                    rcur += rd
                    ccur += cd
        self.nextplayer = self.otherplayer()
        self.data[r][c] = self.player()   

    def terminal(self):
        if len(self.actions()) == 0:
            return True
        else:
            return False
    def countpieces(self, player):
        count = 0
        for r in range(8):
            for c in range(8):
                if self.data[r][c] == player:
                    count += 1
        return count
    def WhoWon(self, player):
        playercount = self.countpieces(player)
        othercount = self.countpieces(1 if player == 2 else 2)
        if playercount == othercount:
            return 0 # Draw
        elif playercount > othercount:
            # return 1000000 # Win
            return 1
        else:
            # return -1000000 # Loss
            return -1
    def print(self):
        print(' ',end='')
        for c in range(8):
            print(c,end='')
        print("")
        for r in range(8):
            print(r,end='')
            for c in range(8):
                if self.data[r][c] == 0:
                    if self.validmove((r,c)):
                        print('⬚',end='')
                    else:
                        print(' ',end='')
                elif self.data[r][c] == 1:
                    print('○',end='')
                elif self.data[r][c] == 2:
                    print('●',end='')
            print(r)
        print(" ",end='')
        for c in range(8):
            print(c,end='')
        print("")
