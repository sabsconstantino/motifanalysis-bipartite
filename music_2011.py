import networkx as nx
import preprocessing as pp
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pp.df_music_HR_11,source='user',target='product')

nodes_U = list(pp.df_music_HR_11['user'].unique())
nodes_O = list(pp.df_music_HR_11['product'].unique())

#---------------------------------------------------------------------
# motif counting

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 

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
plt.hold(False)
plt.loglog(kdist_U.keys(), kdist_U.values(),c='b')
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music2011_u.png')

# plotting degree distribution of users
plt.hold(False)
plt.loglog(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music2011_o.png')

print K
print len(nodes_U)
print len(nodes_O)
print avg_kU
print avg_kO