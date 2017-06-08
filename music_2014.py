import networkx as nx
import preprocessing as pp
import numpy as np

B_m14 = nx.Graph();
B_m14.add_nodes_from(pp.df_music_HR_14['user'].unique(), bipartite=0)
B_m14.add_nodes_from(pp.df_music_HR_14['product'].unique(), bipartite=1)

edges = []
for i in np.arange(0,len(pp.df_music_HR_14.values)):
	edges.append(tuple(pp.df_music_HR_14.values[i]))
	print i

B_m14.add_edges_from(edges)
