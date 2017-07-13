import numpy as np
import networkx as nx
import bip_counter as bc

# example 1
users = np.arange(0,10)
objects = np.arange(10,21)

B1 = nx.Graph()
B1.add_nodes_from(users,bipartite=0)
B1.add_nodes_from(objects,bipartite=1)

edges = [(0,10),(0,11),(1,10),(1,12),(2,12),(2,13),(3,14),(4,12),(4,13),(4,15),(5,15),(5,17),(6,16),(7,16),(8,18),(8,19),(8,20),(9,18),(9,19)]

B1.add_edges_from(edges)

print(bc.count_subgraphs(B1))

# example 2
B2 = nx.bipartite.gnmk_random_graph(500,300,1350)

#print(bc.count_subgraphs(B2))

edges2 = [(0,'a'),(0,'b'),(1,'a'),(1,'b'),(1,'c'),(2,'a'),(2,'b'),(2,'c'),(2,'d'),(3,'c')]
B3 = nx.Graph()
B3.add_edges_from(edges2)
print(bc.count_subgraphs(B3,[0,1,2,3],['a','b','c','d']))