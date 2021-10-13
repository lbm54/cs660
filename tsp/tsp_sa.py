import setup
from random import randint, random
from math import exp

# Tsp is an implementation of the traveling salesman problem using simulated annealing.  
# We are using an integer temperature and just decrementing by one each descent.  The algorithm
# in sa() is similar to the one in the book using probability e^de/temp.  Routes are 
# created using fully connected graphs but with varying edge weights (per our discussion that seemed to be ok?)
# and energies are calculated by evaluating the distances along these routes.  New routes are then generated merely 
# by swapping two cities along the route, and then we either accept the route or (maybe) choose a worse one randomly according to e^de/temp
# and loop again.  Please see setup.py for how the graph, nodes and edges are set up.  Thanks!  Let us know if there are 
# any questions on Slack.
# 
# To run, just call python3 tsp_sa.py 
class tsp():
    nodes = []
    edges = []

    # Setup function.  Creates the nodes, edges, graphs and the first random tour we are to evaluate later
    def __init__(self):
        self.nodes = setup.generateNodes()
        self.edges = setup.generateEdges(self.nodes)
        self.graph = setup.generateGraph(self.edges)
        self.initialTour = setup.randomTour(self.graph)
        # initial temperature is set to a high 100,000 and decrements by one each descent
        self.initialTemperature = 100000

    # Sa stands for simulated annealing.  Following the algorithm in the book
    def sa(self):
        current = self.initialTour
        currentEvaluation = setup.evaluateTour(current, self.graph)
        temperature = self.initialTemperature

        #if we have temperature left
        while temperature > 0:
            #let's make a new route
            candidate = self.swap(current)
            #let's evaluate how good that route is
            candidateEvaluation = setup.evaluateTour(candidate, self.graph)
            #let's create a delta energy
            dE = currentEvaluation - candidateEvaluation

            # we improve the situation
            if (dE > 0): 
                current = candidate
                #then we accept it and move on
                currentEvaluation = candidateEvaluation
            
            #or we don't
            else:
                probability = self.giveMeProbability(dE, temperature)

                # random() is a number between 0 and 1
                randomNum = random()
                if randomNum < probability:
                    current = candidate
                    # we won the coin toss, so we accept and move on
                    currentEvaluation = candidateEvaluation
                temperature = self.schedule(temperature)
        #at the end, just choose the best route we have found so far.  Hopefully it's close to the global value.
        print(f"best route evaluation is: {currentEvaluation}\n")
        return current
            

    # e^dE/temperature
    def giveMeProbability(self, dE, temperature):
        return exp((dE) / temperature)

    #just decrementing one 
    def schedule(self, temperature):
        return temperature - 1

    #simple swap procedure for swapping two cities along a route
    def swap(self, tour):
        randomI1 = 0
        randomI2 = 0

        randomI1 = randint(0, len(tour) - 1)
        randomI2 = randint(0, len(tour) - 1)

        if randomI1 == randomI2:
            randomI1 = randomI1 - 1 if randomI1 > 0 else randomI1 + 1

        temp = tour[randomI1]
        tour[randomI1] = tour[randomI2]
        tour[randomI2] = temp
        return tour

tsp = tsp()
print(tsp.sa())


