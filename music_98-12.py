import networkx as nx
import preprocessing_cumulative as pc
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pc.df_m_12,source='user',target='product')

nodes_U = list(pc.df_m_12['user'].unique())
nodes_O = list(pc.df_m_12['product'].unique())

#---------------------------------------------------------------------
# motif counting

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 
#[  1.41884100e+06   1.80095150e+07   3.16060478e+11   1.70624832e+12
#   6.15144000e+05   9.43168500e+07]

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
plt.xlim([-10,10000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music98-12_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,10000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music98-12_o.png')

print K # 343777
print len(nodes_U) # 222894
print len(nodes_O) # 94753
print avg_kU # 1.54233402424
print avg_kO # 3.62813842306