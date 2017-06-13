import networkx as nx
import preprocessing_cumulative as pc
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pc.df_m_14,source='user',target='product')

nodes_U = list(pc.df_m_14['user'].unique())
nodes_O = list(pc.df_m_14['product'].unique())

#---------------------------------------------------------------------
# motif counting

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 
#[  3.03368900e+06   2.99905840e+07   1.32276086e+12   7.48477016e+12
#   7.22309000e+05   1.54532781e+08]

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
plt.savefig('plots/pk_music98-14_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,10000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music98-14_o.png')

print K # 744929
print len(nodes_U) # 436127
print len(nodes_O) # 249582
print avg_kU # 1.70805522245
print avg_kO # 2.98470642915