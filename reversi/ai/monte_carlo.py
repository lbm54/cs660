from math import sqrt, log
from ai.reversiBoardGroup4 import RBoardGroup4
import random

class Node:
    def __init__(self, moveThatGotUsHere = None, parent = None, currentBoard = None):
        self.winsFromHere = 0
        self.timesVisited = 0

        self.parent = parent 
        self.children = []

        self.moveThatGotUsHere = moveThatGotUsHere 
        self.unseenMoves = currentBoard.actions()
        self.playerJustMoved = currentBoard.otherplayer()
    
    def selectChild(self):
        #balance between exploration and explotation: x_j += sqrt(2ln(n)/n_i)
        #[-1] means access from the end of the list
        retVal = sorted(self.children, key = lambda node: node.winsFromHere/node.timesVisited + sqrt(2 * log(self.timesVisited)/node.timesVisited))[-1]
        return retVal

    # we're building a stats tree at this point, and let's now consider this node and add it to the tree
    def expandThisNode(self, moveThatGotUsHere, theStateAtThatPoint):
        #first create the node (the parent is self because we are calling this from the parent node)
        newNode = Node(moveThatGotUsHere, parent = self, state = theStateAtThatPoint)
        self.potentialMoves.remove(moveThatGotUsHere)
        self.children.append(newNode)

    #in monte carlo we will update or backpropagate all the way up the tree calling this method for each node
    def updateThisNode(self, whatHappened):
        self.timesVisited += 1
        self.winsFromHere += whatHappened

class MonteCarloTreeSearch():
    def __init__(self, board, howManyTimes):
        self.initialBoard = board
        self.howManyTimes = howManyTimes
        self.initialNode = Node(currentBoard = board)
        currentNode = self.initialNode
         #copying board and using our own version
        currentState = RBoardGroup4(self.initialBoard)
        self.select(currentNode, currentState)
           
    # Select
    #when all the child nodes have been visited at least once.  Ai can select which child node to be investigated further.
    #the higher the value, the better the move is for producing a win

    #two criteria: 
    # 1) how good are the stats?
    # 2) how much has this child node been ignored?

    #we then call expansion on that child node because it may have nodes it hasn't explored yet and the process repeats
    # expansion --> simulation --> update --> selection
    # https://www.youtube.com/watch?v=Fbs4lnGLS8M
    def select(self, currentNode, currentBoard):
        
        #at the beginning, our initial node has unseenmoves but we don't have any children
        #so currentNode.unseenMoves != [] and currentNode.childNodes == [], so we don't do this
        #however as we iterate, we are changing the currentnode, so we will come back later
        while currentNode.unseenMoves == [] and currentNode.childNodes != []:
            currentNode = currentNode.selectChild()
            currentBoard.simResult(currentNode.moveThatGotUsHere)
        self.expand(currentNode, currentBoard)

    #if we can expand, we do
    def expand(self, currentNode, currentBoard):
        #at the beginning, there will be unseenmoves
        if currentNode.unseenMoves != []: 
            move = random.choice(currentNode.unseenMoves) 
            currentBoard.simResult(move)
            #expandthisnode will remove the move from unseen moves and will add the node to children
            currentNode = currentNode.expandThisNode(move, currentBoard)
        self.simulate(currentNode, currentBoard)

    def simulate(self, currentNode, currentBoard):
        while currentBoard.actions() != []: #while we have actions to look at
            currentBoard.simResult(random.choice(currentBoard.actions()))
        self.update(currentNode, currentBoard)

    def update(self, currentNode, currentBoard):
        result = currentBoard.whoWon()
        while currentNode != None: # backpropagate from the expanded node and work back to the root node
            node.updateThisNode(result) # state is terminal. Update node with result from POV of node.playerJustMoved
            node = node.parent