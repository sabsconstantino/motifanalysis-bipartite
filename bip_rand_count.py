import networkx as nx
import random
from collections import Counter, OrderedDict
import bip_counter as bc
import numpy as np
from datetime import datetime as dt

# This module is generating samples from ensembles of random graphs, and for computing the zscores of the subgraph counts.

def rand_samedegrees(df, col1, col2, fname, fname_start=0, fname_end=100):
    stubs_U = list(df[col1])
    stubs_O = list(df[col2])
    stubs_U.sort(key=Counter(stubs_U).get,reverse=False)
    stubs_O.sort(key=Counter(stubs_O).get,reverse=False)

    R = nx.Graph()
    R.add_nodes_from(set(stubs_U), bipartite='u')
    R.add_nodes_from(set(stubs_O), bipartite='o')
    
    nodes_O = Counter(stubs_O).most_common()

    num_graphs = 0

    while num_graphs < (fname_end - fname_start):
        print num_graphs
        k_U = Counter(stubs_U)

        edges = []
        for o in nodes_O:
            print o
            users = np.random.choice(k_U.keys(),o[1],replace=False)
            edges.extend(zip( [o[0]]*o[1], users) )
            for u in users:
                if k_U[u] == 1:
                    del k_U[u]
                else:
                    k_U[u] = k_U[u]-1

        R.add_edges_from(edges)
        nx.write_gml(R,fname + str(num_graphs + fname_start) + ".gml")
        num_graphs += 1

def rand_sameU_randO(df, col1, col2, fname, fname_start=0, fname_end=100):
    k_U = Counter(list(df[col1]))
    nodes_U = list(df[col1].unique())
    nodes_O = list(df[col2].unique())

    R = nx.Graph()
    R.add_nodes_from(nodes_O, bipartite='u')
    R.add_nodes_from(nodes_U, bipartite='o')
    
    num_graphs = 0

    while num_graphs < (fname_end - fname_start):
        print num_graphs

        edges = []
        for u in k_U.keys():
            print u
            objects = np.random.choice(nodes_O,k_U[u],replace=False)
            edges.extend(zip( [u]*k_U[u], objects) )

        R.add_edges_from(edges)
        nx.write_gml(R,fname + str(num_graphs + fname_start) + ".gml")
        num_graphs += 1

def get_zscores(count_from_data,fname,fname_start=0,fname_end=100,nodes_U=None,nodes_O=None):
    num_subgraphs = len(count_from_data)
    num_rg = fname_end - fname_start
    ensemble_counts = np.zeros([num_rg,num_subgraphs],dtype=np.int64)
    i = 0
    while i < num_rg:
        nth = fname_start + i
        G = nx.read_gml(fname + str(nth) + ".gml")
        ensemble_counts[i] = bc.count_subgraphs(G, nodes_U=nodes_U, nodes_O=nodes_O)
        print str(nth) +' '+ str(dt.now())
        i += 1
        del G

    zscores = np.zeros(num_subgraphs,dtype=np.float64)
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)

    zscores = (count_from_data - mjus) / sigmas

    return zscores