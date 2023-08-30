import networkx as nx
import matplotlib.pyplot as plt
import queue
from collections import deque

def BFS(g, start):

    g = nx.Graph(g)
    nextNodes = queue.Queue(0)
    nodesVisited = []
    nextNodes.put(start)

    while not nextNodes.empty():
        current = nextNodes.get()
        queue2list = list(nextNodes.queue)
        for node in g.neighbors(current):
            if node not in nodesVisited and node not in queue2list:
                nextNodes.put(node)      
        nodesVisited.append(current)

    return nodesVisited