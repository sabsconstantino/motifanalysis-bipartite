import networkx as nx
import preprocessing as pp
import numpy as np
import bip_counter as bc
from collections import Counter
import matplotlib.pyplot as plt

B = nx.from_pandas_dataframe(pp.df_music_HR_09,source='user',target='product')

nodes_U = list(pp.df_music_HR_09['user'].unique()) 
nodes_O = list(pp.df_music_HR_09['product'].unique())

#---------------------------------------------------------------------
# motif counting

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 
# [  3.11630000e+04   4.78968000e+05   5.92180103e+08   5.60041815e+09  
#    1.36400000e+03   3.16141000e+05]

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
plt.savefig('plots/pk_music2009_u.png')

# plotting degree distribution of users
plt.figure()
plt.xscale('log')
plt.yscale('log')
plt.scatter(kdist_O.keys(), kdist_O.values(),c='r')
plt.xlim([-10,1000])
plt.xlabel("k")
plt.ylabel("P(k)")
plt.savefig('plots/pk_music2009_o.png')

print K # 24676
print len(nodes_U) # 19024
print len(nodes_O) # 11695
print avg_kU # 1.29709840202
print avg_kO # 2.10996152202