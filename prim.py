import networkx as nx
import math

def prim(g):
    minWeight = math.inf
    g = nx.Graph(g)
    cost = 0
    edges = []
    mstNodes = [list(g)[0]]

    print(mstNodes)
    print(list(g))
    
    while len(mstNodes) != len(list(g)): #not every node in mst
        for u in mstNodes:
            for v in g.neighbors(u): #every "seen" node
                if not v in mstNodes: #v otuside but u inside
                    if minWeight > g[u][v]["weight"]:
                        minWeight = g[u][v]["weight"]
                        x = u
                        y = v
        mstNodes.append(y)
        print(mstNodes)
        edges.append((x,y,minWeight))
        cost += minWeight
        minWeight = math.inf

    return cost, edges

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


print(prim(G))
