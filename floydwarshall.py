import networkx as nx
import matplotlib.pyplot as plt
import math

def fw(g):
    g = nx.DiGraph(g)
    distance = {}
    v = g.number_of_nodes()

    for node in g.nodes():
        distance[node]={}
        for node2 in g.nodes():
            if g.has_edge(node,node2):
                distance[node][node2] = g.edges[node,node2].get("weight",math.inf)
            elif node == node2:
                distance[node][node2] = 0
            else:
                distance[node][node2] = math.inf

    for i in g.nodes():
        for j in g.nodes():
            for k in g.nodes():
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

G = nx.Graph()
G.add_edge(4,5,weight=3.5) 
G.add_edge(4,7,weight=3.7) 
G.add_edge(5,7,weight=2.8) 
G.add_edge(0,7,weight=1.6) 
G.add_edge(1,5,weight=3.2) 
G.add_edge(0,4,weight=3.8) 
G.add_edge(2,3,weight=1.7) 
G.add_edge(1,7,weight=1.9) 
G.add_edge(0,2,weight=2.6) 
G.add_edge(1,2,weight=3.6) 
G.add_edge(1,3,weight=2.9) 
G.add_edge(2,7,weight=3.4) 


print(fw(G))