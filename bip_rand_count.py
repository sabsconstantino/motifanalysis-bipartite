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

def rand_sameU_randO(df, col1, col2, fname=None, fname_start=0, fname_end=100):
    stubs_U = list(df[col1])
    nodes_O = list(df[col2].unique())

    num_edges = len(stubs_U)
    rej_threshold = int(len(stubs_U) * 0.1)
    ensemble_sample = [] 

    while len(ensemble_sample) < (fname_end - fname_start):
        print len(ensemble_sample)
        print(rej_threshold)
        edges = []
        rejected_edges = 0
        reject_graph = False
        R = nx.Graph()
        stubs_O = np.random.choice(nodes_O, num_edges, replace=True)
        R.add_edges_from(zip(stubs_U,stubs_O))
        if len(R.edges()) < num_edges - rej_threshold:
            reject_graph = True
            break
        else:
            # get stubs remaining
            stubs_in = [e[0] for e in R.edges()]
            c_all = Counter(stubs_U)
            c_in = Counter(stubs_in)
            remaining_stubs = list((c_all-c_in).elements())
            rej_ct = len(remaining_stubs)
            while remaining_stubs:
                print(len(remaining_stubs))
                stubs_O = np.random.choice(nodes_O, len(remaining_stubs), replace=True)
                prev_edgect = len(R.edges())
                R.add_edges_from(zip(stubs_U,stubs_O))
                rej_ct += (len(R.edges()) - prev_edgect)
                print rej_ct
                if rej_ct > rej_threshold:
                    reject_graph = True
                    break
                else:
                    stubs_in = [e[0] for e in R.edges()]
                    c_in = Counter(stubs_in)
                    remaining_stubs = list((c_all-c_in).elements())

        if not reject_graph:
            if fname != None:
                nx.write_gml(R,fname + str(len(ensemble_sample) + fname_start) + ".gml")
            ensemble_sample.append(R) 

    return ensemble_sample 

def get_zscores(count_from_data,rand_ensemble,nodes_U=None,nodes_O=None):
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    num_subgraphs = len(count_from_data)
    ensemble_counts = np.zeros([len(rand_ensemble),num_subgraphs],dtype=int)
    for i in np.arange(len(ensemble_counts)):
        print i
        ensemble_counts[i] = bc.count_subgraphs(rand_ensemble[i], nodes_U, nodes_O)    

    zscores = np.zeros(num_subgraphs,dtype=np.float64)
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)

    zscores = (count_from_data - mjus) / sigmas

    return zscores