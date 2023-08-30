from queue import PriorityQueue as pq
import networkx as nx
import matplotlib.pyplot as plt


def bestFirstSearch(g, start, end):
    g = nx.Graph(g)
    print(nx.to_dict_of_dicts(g))
    toVisit = pq()
    toVisit.put((0,start))
    visited = []
    predecessor = {}

    while not toVisit.empty():
        current = toVisit.get()[1]
        visited.append(current)

        for neighbour in g[current]:
            if neighbour not in visited:
                predecessor[neighbour]=current

                nodeweight = g.nodes[neighbour]["weight"] #heuristic here
                
                toVisit.put((nodeweight,neighbour))
                if neighbour==end:
                    print("found")
                    return predecessor, visited

