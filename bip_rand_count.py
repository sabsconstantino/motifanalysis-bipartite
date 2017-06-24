import networkx as nx
import random
from collections import Counter
import bip_counter as bc
import numpy as np

# This module is generating samples from ensembles of random graphs, and for computing the zscores of the subgraph counts.

def rand_samedegrees(df, col1, col2):
    nodes_U = list(df[col1])
    nodes_O = list(df[col2])
    nodes_O.sort(key=Counter(nodes_O).get,reverse=False) # https://stackoverflow.com/questions/23429426/sorting-a-list-by-frequency-of-occurrence-in-a-list    

    ensemble_sample = []    

    while len(ensemble_sample) < 100:
        print len(ensemble_sample)
        sU = list(nodes_U)
        sO = list(nodes_O)
        edges = []
        while sO and sU:
            random.shuffle(sU)
            if (sU[-1],sO[-1]) not in edges:
                edges.append((sU.pop(), sO.pop()))
        R = nx.Graph()
        R.add_edges_from(edges)
        ensemble_sample.append(R) 

    return ensemble_sample  

def get_zscores(count_from_data,rand_ensemble,nodes_U=None,nodes_O=None):
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    ensemble_counts = np.zeros([len(rand_ensemble),4],dtype=int)
    for i in np.arange(len(ensemble)):
        print i
        ensemble_counts[i] = bc.count_subgraphs(rand_ensemble[i], nodes_U, nodes_O)    

    zscores = np.zeros(4,dtype=np.float64)
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)

    zscores = (count_from_data - mjus) / sigmas

    return zscores