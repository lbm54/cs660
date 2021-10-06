from typing import Final
from random import randint
from math import sqrt

NUM_NODES: Final = 100
MAX_X: Final = 100
MAX_Y: Final = 100

def generateNodes():
    nodes = set()
    for i in range(NUM_NODES):
        x = randint(0, MAX_X)
        y = randint(0, MAX_Y)
        nodes.add((f"node{i}", (x, y)))
    return list(nodes)

#FIXME -- are we ok with a fully connected graph?
def generateEdges(nodes):
    edges = set()
    for start in nodes:
        for end in nodes:
            if (end, start) not in edges: edges.add((start, end))

    return list(edges)

def generateGraph(edges):
    graph = {}
    for edge in edges:

        #calculate euclidian distance between nodes
        node1 = edge[0]
        node2 = edge[1]
        dx2 = (node1[1][0] - node2[1][0])**2
        dy2 = (node1[1][1] - node2[1][1])**2
        distance = int(sqrt(dx2 + dy2))

        node1Name = node1[0]
        node2Name = node2[0]
        if node1Name not in graph: 
            graph[node1Name] = {}
            graph[node1Name][node2Name] = distance
        else: graph[node1Name][node2Name] = distance

        if node2Name not in graph: 
            graph[node2Name] = {}
            graph[node2Name][node1Name] = distance
        else: graph[node2Name][node1Name] = distance
    return graph

def randomTour(graph):
    tour = []
    nodes = list(graph.keys())
    while len(nodes) > 0:
        tour.append(nodes.pop(randint(0, len(nodes) - 1)))
    return tour

def evaluateTour(tour, graph):
    totalDistance = 0
    for i in range(len(tour) - 2):
        current = tour[i]
        next = tour[i + 1]
        totalDistance = totalDistance + graph[current][next]
    return totalDistance

# nodes = generateNodes()
# edges = generateEdges(nodes)
# graph = generateGraph(edges)
# tour = randomTour(graph)
# evaluateTour(tour, graph)