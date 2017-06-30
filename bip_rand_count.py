import networkx as nx
import random
from collections import Counter
import bip_counter as bc
import numpy as np

# This module is generating samples from ensembles of random graphs, and for computing the zscores of the subgraph counts.

def rand_samedegrees(df, col1, col2, fname=None, fname_start=0, fname_end=100):
    stubs_U = list(df[col1])
    stubs_O = list(df[col2])
    stubs_O.sort(key=Counter(stubs_O).get,reverse=False) # https://stackoverflow.com/questions/23429426/sorting-a-list-by-frequency-of-occurrence-in-a-list     

    rej_threshold = int(len(stubs_O) * 0.1)
    print rej_threshold
    ensemble_sample = [] 

    while len(ensemble_sample) < (fname_end - fname_start):
        print len(ensemble_sample)
        sU = list(stubs_U)
        sO = list(stubs_O)
        edges = []
        rejected_edges = 0
        reject_graph = False
        while sO and sU:
            if (sU[-1],sO[-1]) not in edges:
                edges.append((sU.pop(), sO.pop()))
                print len(edges)
            else: 
                random.shuffle(sU)               
                rejected_edges += 1
            if rejected_edges > rej_threshold:
                reject_graph = True
                break


        if not reject_graph:
            R = nx.Graph()
            R.add_edges_from(edges)
            if fname != None:
                nx.write_gml(R,fname + str(len(ensemble_sample) + fname_start) + ".gml")
            ensemble_sample.append(R) 

    return ensemble_sample  

def get_zscores(count_from_data,rand_ensemble,nodes_U=None,nodes_O=None):
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    ensemble_counts = np.zeros([len(rand_ensemble),4],dtype=int)
    for i in np.arange(len(ensemble_counts)):
        print i
        ensemble_counts[i] = bc.count_subgraphs(rand_ensemble[i], nodes_U, nodes_O)    

    zscores = np.zeros(4,dtype=np.float64)
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)

    zscores = (count_from_data - mjus) / sigmas

    return zscores