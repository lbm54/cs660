#Setup creates the nodes, edges and graph that we will use later, as well as
#evaluating routes and creating an initial route.

from typing import Final
from random import randint
from math import sqrt

NUM_NODES: Final = 100
MAX_X: Final = 100
MAX_Y: Final = 100

#nodes are of the form (nodei, (x, y))
def generateNodes():
    nodes = set()
    for i in range(NUM_NODES):
        x = randint(0, MAX_X)
        y = randint(0, MAX_Y)
        nodes.add((f"node{i}", (x, y)))
    return list(nodes)

#edges are of the form (start, end)
def generateEdges(nodes):
    edges = set()
    for start in nodes:
        for end in nodes:
            if (end, start) not in edges: edges.add((start, end))

    return list(edges)

#the graph is a big dictionary filled with dictionaries of edges
#and weights calculated by euclidian distance between nodes
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

#walks through the graph and returns a list of cities
def randomTour(graph):
    tour = []
    nodes = list(graph.keys())
    while len(nodes) > 0:
        tour.append(nodes.pop(randint(0, len(nodes) - 1)))
    return tour

#walks through the tour and sums up the weights between the cities
def evaluateTour(tour, graph):
    totalDistance = 0
    for i in range(len(tour) - 2):
        current = tour[i]
        next = tour[i + 1]
        totalDistance = totalDistance + graph[current][next]
    return totalDistance
