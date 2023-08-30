import networkx as nx
import math
from queue import PriorityQueue

def dijkstra2(g,start): #pq
    predecessor = {}
    distance = {}
    getWeight = nx.get_edge_attributes(g,"weight")
    g = nx.DiGraph(g)
    toVisit = PriorityQueue()
    visited = []

    for item in list(g.nodes()):
        distance[item]=math.inf
    distance[start]=0
    toVisit.put((0,start))

    while not toVisit.empty():
        current = toVisit.get()[1]
        visited.append(current)
        for (u,v) in g.out_edges(current):
            if v not in visited:
                print(current, v)
                tentative = distance[current]+g[u][v]["weight"]
                if distance[v] > tentative:
                    distance[v]=tentative
                    predecessor[v]=current
                    toVisit.put((tentative,v))
    
    return distance




def georgiasDijkstra(G,startNode):
  unvisitedNodes = list(G.nodes)
  shortestPath = {} # distance on each node while processing so far
  previousNodes = {} # shortest known path previous node to current node so far
 
  for node in unvisitedNodes:
    shortestPath[node] = math.inf # initialise all nodes distance to infinity
    shortestPath[startNode] = 0 # starting node's distance initialise with 0
    
  while unvisitedNodes:
    # find the node with the lowest distance so far
    currentMinNode = None
    for node in unvisitedNodes: # Iterate over the nodes
      if currentMinNode == None:
        currentMinNode = node
      elif shortestPath[node] < shortestPath[currentMinNode]:
        currentMinNode = node
                
    for V in G.neighbors(currentMinNode):
      tentativeValue = shortestPath[currentMinNode] + G[currentMinNode][V]['weight']
      if tentativeValue < shortestPath[V]:
        shortestPath[V] = tentativeValue # relax the edges
        previousNodes[V] = currentMinNode # save path
 
    unvisitedNodes.remove(currentMinNode) # remove the processed node from unvisited
    
  return previousNodes, shortestPath

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


print(dijkstra2(G,3))