import networkx as nx
import preprocessing as pp
import numpy as np
import bip_counter as bc
from collections import Counter


B = nx.from_pandas_dataframe(pp.df_music_HR_09,source='user',target='product')

nodes_U = list(pp.df_music_HR_09['user'].unique()) # len(nodes_U): 19024
nodes_O = list(pp.df_music_HR_09['product'].unique()) # len(nodes_O): 11695

#---------------------------------------------------------------------
# motif counting
'''
motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)

print motifs 
# [  3.11630000e+04   4.78968000e+05   5.92180103e+08   5.60041815e+09   1.36400000e+03   3.15459000e+05]
'''

#---------------------------------------------------------------------
# exploratory graph analysis

# no. of edges
K = len(B.edges()) # 24676

# degrees
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

# average degree
avg_kU = sum(k_U.values()) / (len(nodes_U)*1.00)
avg_kO = sum(k_O.values()) / (len(nodes_O)*1.00)

# degree distribution
kcount_U = dict(Counter(k_U.values()))
kdist_O = {k:v/(K*1.0) for k,v in kcount_U.iteritems()}

kcount_O = dict(Counter(k_O.values()))
kdist_O = {k:v/(K*1.0) for k,v in kcount_O.iteritems()}