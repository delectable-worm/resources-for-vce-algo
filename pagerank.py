import networkx as nx
import matplotlib.pyplot as plt
import math

def pagerank(g, i = 1, d=0.85):

    g=nx.DiGraph(g)
    weight = {}
    bweight = {}

    #init
    for n in g.nodes():
        weight[n]=(1)/g.number_of_nodes()
        if g.out_degree(n) == 0:
            for n2 in g.nodes():
                g.add_edge(n,n2)
    
    #iter
    for j in range(i):
        for n in g.nodes():
            sumn = (1-d)/g.number_of_nodes()
            for (u,v) in g.in_edges(n):
                sumn += d*weight[u]/g.out_degree(u)
            bweight[n] = sumn
        for key in bweight:
            weight[key]=bweight[key]
        print(weight)
    
    #sum check
    sum = 0
    for j in weight:
        sum += weight[j]
        weight[j]=round(weight[j],5)

    print(sum)
    return weight

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


print(pagerank(G))