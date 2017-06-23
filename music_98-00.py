import networkx as nx
import preprocessing_cumulative as pc
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pc.df_m_00,source='user',target='product')

nodes_U = list(pc.df_m_00['user'].unique())
nodes_O = list(pc.df_m_00['product'].unique())

#---------------------------------------------------------------------
# exploratory graph analysis

# no. of edges
K = len(B.edges())

# degrees
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

# average degree
avg_kU = sum(k_U.values()) / (len(nodes_U)*1.00)
avg_kO = sum(k_O.values()) / (len(nodes_O)*1.00)

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
plt.savefig('plots/pk_music98-00_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,1000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music98-00_o.png')

# Printing to file
mfile = open('motifdata_music.csv',mode='a')
mfile.write('1998-2000,' + str(K) + ',' + str(len(nodes_U)) + ',' + str(len(nodes_O)) + ',' + str(avg_kU) + ',' + str(avg_kO) + ',')

#---------------------------------------------------------------------
# motif counting
motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)
s = str(motifs)
s = s.replace('[','')
s = s.replace(']','')
s = s.split()

for i in np.arange(len(s)-1):
	mfile.write(s[i] + ',')
mfile.write(s[-1])
mfile.write('\n')