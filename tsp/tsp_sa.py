import setup
from random import randint, random
from math import exp

class tsp():
    nodes = []
    edges = []
    # distances = {}

    def __init__(self):
        self.nodes = setup.generateNodes()
        self.edges = setup.generateEdges(self.nodes)
        self.graph = setup.generateGraph(self.edges)
        self.initialTour = setup.randomTour(self.graph)
        self.initialTemperature = 100000

    def sa(self):
        current = self.initialTour
        currentEvaluation = setup.evaluateTour(current, self.graph)
        temperature = self.initialTemperature
        while temperature > 0:
            candidate = self.swap(current)
            candidateEvaluation = setup.evaluateTour(candidate, self.graph)
            dE = currentEvaluation - candidateEvaluation

            # we improve the situation
            if (dE > 0): 
                current = candidate
                currentEvaluation = candidateEvaluation
            
            #or we don't
            else:
                probability = self.giveMeProbability(dE, temperature)

                # random() is a number between 0 and 1
                randomNum = random()
                if randomNum < probability:
                    current = candidate
                    currentEvaluation = candidateEvaluation
                temperature = self.schedule(temperature)
        print(f"best route evaluation is: {currentEvaluation}\n")
        return current
            

    # e^dE/temperature
    def giveMeProbability(self, dE, temperature):
        return exp((dE) / temperature)

    def schedule(self, temperature):
        return temperature - 1

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


