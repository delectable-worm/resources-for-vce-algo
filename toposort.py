import networkx as nx
import matplotlib.pyplot as plt

def toposort(g):
    g = nx.DiGraph(g)
    nodes = []
    if g.nodes(): #"base case check"
        for n in g.nodes():
            if g.in_degree(n) == 0:
                nodes.append(n)
        for n in nodes: #because you can't change the iter var during iter
            g.remove_node(n)
        nodes.append(toposort(g)) #recur
    return nodes

g = nx.DiGraph()
g.add_edges_from([
    (1,2),
    (2,3),
    (3,4),
    (1,5)
])

print(toposort(g))