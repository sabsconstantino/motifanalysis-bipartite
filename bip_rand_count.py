import networkx as nx
import preprocessing_cumulative as pc
import random
from collections import Counter
import bip_counter as bc
import numpy as np
from scipy import stats

# This module is generating samples from ensembles of random graphs, and for computing the zscores of the motif counts.

def rand_samedegrees(df, col1, col2):
    nodes_U = list(df[col1])
    nodes_O = list(df[col2])
    nodes_O.sort(key=Counter(nodes_O).get,reverse=False) # https://stackoverflow.com/questions/23429426/sorting-a-list-by-frequency-of-occurrence-in-a-list    

    ensemble_sample = []    

    while len(ensemble_sample) < 100:
        sU = list(nodes_U)
        sO = list(nodes_O)
        edges = []
        while sO:
            random.shuffle(sU)
            if (sU[-1],sO[-1]) not in edges:
                edges.append((sU.pop(), sO.pop()))
        R = nx.Graph()
        R.add_edges_from(edges)
        ensemble_sample.append(R) 

    return R   

def get_zscore(R,nodes_O=None,nodes_U=None)
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    counts = np.zeros([len(ensemble_sample),4],dtype=int)
    for i in np.arange(len(ensemble_sample)):
        counts[i] = bc.count_motifs(R, nodes_U, nodes_O)    

    zscores = np.zeros([len(ensemble_sample),4])
    for i in np.arange(4):
    	zscores[:,i] = stats.zscore(counts[:,i])

    return zscores
