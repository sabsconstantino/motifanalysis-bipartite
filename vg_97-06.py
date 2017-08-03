import networkx as nx
import preprocessing_cumulative as pc
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

nodes_U = list(pc.df_vg_06['user'].unique())
nodes_O = list(pc.df_vg_06['product'].unique())

num_U = len(nodes_U)
num_O = len(nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_06,source='user',target='product')
nx.set_node_attributes(B, 'bipartite', dict(zip(nodes_U,['u']*num_U)))
nx.set_node_attributes(B, 'bipartite', dict(zip(nodes_O,['o']*num_O)))

#---------------------------------------------------------------------
# exploratory graph analysis

# no. of edges
K = len(B.edges())

# degrees
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

# average degree
avg_kU = sum(k_U.values()) / (num_U*1.00)
avg_kO = sum(k_O.values()) / (num_O*1.00)

# degree distribution
kcount_U = dict(Counter(k_U.values()))
kdist_U = {k:v/(K*1.0) for k,v in kcount_U.iteritems()}

kcount_O = dict(Counter(k_O.values()))
kdist_O = {k:v/(K*1.0) for k,v in kcount_O.iteritems()}

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_U.keys(), kdist_U.values(),c='b')
plt.xlim([-10,1000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_vg97-06_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,1000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_vg97-06_o.png')

#---------------------------------------------------------------------
# subgraph counting
subgraphs = bc.count_subgraphs(B)
s = str(subgraphs)
s = s.replace('[','')
s = s.replace(']','')
s = s.split()

# Printing to file
mfile = open('subgraphdata_videogames.csv',mode='a')
mfile.write('1997-2006,' + str(K) + ',' + str(num_U) + ',' + str(num_O) + ',' + str(avg_kU) + ',' + str(avg_kO) + ',')
for i in np.arange(len(s)-1):
	mfile.write(s[i] + ',')
mfile.write(s[-1])
mfile.write('\n')