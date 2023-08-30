import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
import math

def bf(g, start):
    predecessor = {}
    distance = {}
    g = nx.DiGraph(g)

    for node in g.nodes():
        distance[node] = math.inf
    distance[start]=0

    for i in range(g.number_of_nodes()-1):
        for (u,v,d) in g.edges.data("weight"):
            if distance[u] + d < distance[v]:
                distance[v]=distance[u]+d
                predecessor[v]=u

    for (u,v,d) in g.edges.data("weight"):
            if distance[u] + d < distance[v]:
                return 1
    
    return predecessor,distance