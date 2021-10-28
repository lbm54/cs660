from math import sqrt, log
from ai.reversiBoardGroup4 import RBoardGroup4
import random

class Node:
    def __init__(self, moveThatGotUsHere = None, parent = None, currentState = None):
        self.winsFromHere = 0
        self.timesVisited = 0
        self.parent = parent 
        self.children = []

        self.moveThatGotUsHere = moveThatGotUsHere 
        self.unseenMoves = currentState.actionsNoSet()
    
    def selectChild(self):
        #x_j += sqrt(2ln(n)/n_i)
        #[-1] means access from the end of the list
        retVal = sorted(self.children, key = lambda node: node.winsFromHere/node.timesVisited + sqrt(2 * log(self.timesVisited)/node.timesVisited))[-1]
        return retVal

    # we're building a stats tree at this point, and let's now consider this node and add it to the tree
    def expandThisNode(self, moveThatGotUsHere, theStateAtThatPoint):
        #first create the node (the parent is self because we are calling this from the parent node)
        newNode = Node(moveThatGotUsHere = moveThatGotUsHere, parent = self, currentState = theStateAtThatPoint)
        self.unseenMoves.remove(moveThatGotUsHere)
        self.children.append(newNode)
        return newNode

    #in monte carlo we will update or backpropagate all the way up the tree calling this method for each node
    def updateThisNode(self, whatHappened):
        self.timesVisited += 1
        self.winsFromHere += whatHappened


class MCT():

    def __init__(self, state):
        self.player = state.player()

    # Select
    #when all the child nodes have been visited at least once.  Ai can select which child node to be investigated further.
    #the higher the value, the better the move is for producing a win

    #two criteria: 
    # 1) how good are the stats?
    # 2) how much has this child node been ignored?

    #we then call expansion on that child node because it may have nodes it hasn't explored yet and the process repeats
    # expansion --> simulation --> update --> selection
    # https://www.youtube.com/watch?v=Fbs4lnGLS8M
    def select(self, currentNode, currentState):
        
        #at the beginning, our initial node has unseenmoves but we don't have any children
        #so currentNode.unseenMoves != [] and currentNode.childNodes == [], so we don't do this
        #however as we iterate, we are changing the currentnode, so we will come back later
        while currentNode.unseenMoves == [] and currentNode.children != []:
            currentNode = currentNode.selectChild()

            #this is changing player just moved
            currentState.simResult(currentNode.moveThatGotUsHere)
        self.expand(currentNode, currentState)

    #if we can expand, we do
    def expand(self, currentNode, currentState):
        #at the beginning, there will be unseenmoves
        if currentNode.unseenMoves != []: 
            move = random.choice(currentNode.unseenMoves) 
            currentState.simResult(move)
            #expandthisnode will remove the move from unseen moves and will add the node to children
            currentNode = currentNode.expandThisNode(move, currentState)
        self.simulate(currentNode, currentState)

    def simulate(self, currentNode, currentState):
        while True: #while we have actions to look at
            #this will update current state, and then actionsNoSet will be different
            actions = currentState.actionsNoSet()

            if actions != []:
                currentState.simResult(random.choice(actions))
            else: break
        self.update(currentNode, currentState)

    def update(self, currentNode, currentState):

        #from the perspective of the player who moved at that point
        #FIXME: is who won actually returning the right thing?
        action = currentState.whoWon(self.player)
        while currentNode != None: # backpropagate from the expanded node and work back to the root node
            currentNode.updateThisNode(action)
            currentNode = currentNode.parent

def monteCarloTreeSearch(state, howManyTimes):
    initialState = RBoardGroup4(rboard = state)
    initialNode = Node(currentState = initialState)
    mct = MCT(initialState)

    for i in range(howManyTimes):
        currentNode = initialNode
        currentState = RBoardGroup4(initialState)
        mct.select(currentNode, currentState)
    val = sorted(initialNode.children, key = lambda c: c.timesVisited)[-1].moveThatGotUsHere
    return val