import networkx as nx
import matplotlib.pyplot as plt

def DFS(g,s):
    visited = []
    seen = [s]
    while len(seen)!=0:
        current = seen.pop()
        visited.append[current]
        for neighbour in g.neighbours(current):
            if neighbour not in visited:
                seen.append(neighbour)

def DFSr(g, s, visited):
    visited.append(s)
    g = nx.DiGraph(g)
    for neighbour in g.neighbors(s):
        if neighbour not in visited:
            visited = DFSr(g,neighbour,visited)
    return visited

def DFSrWithBreak(g,s, target, out=False,visited=[]): #nicer version with parameter
    visited.append(s)
    g = nx.DiGraph(g)
    if s == target:
        out = True
        return visited
    for neighbour in g.neighbors(s):
        if out:
            return visited
        else:
            visited = DFSrWithBreak(g,neighbour,visited,out)
    return visited