import networkx as nx
import preprocessing_cumulative as pc
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pc.df_m_09,source='user',target='product')

nodes_U = list(pc.df_m_09['user'].unique())
nodes_O = list(pc.df_m_09['product'].unique())

#---------------------------------------------------------------------
# motif counting

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 
#[  8.06168000e+05   1.31392170e+07   9.77068053e+10   2.75350305e+11
#   4.92371000e+05   6.30130560e+07]

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
plt.savefig('plots/pk_music98-09_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,10000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music98-09_o.png')

print K # 187627
print len(nodes_U) # 121357
print len(nodes_O) # 20967
print avg_kU # 1.54607480409
print avg_kO # 8.94868126103