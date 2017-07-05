import networkx as nx
import random
from collections import Counter, OrderedDict
import bip_counter as bc
import numpy as np

# This module is generating samples from ensembles of random graphs, and for computing the zscores of the subgraph counts.

def rand_samedegrees(df, col1, col2, fname, pct_cap=1, fname_start=0, fname_end=100):
    nodes_U = list(df[col1].unique())
    nodes_O = list(df[col2].unique())

    stubs_U = list(df[col1])
    stubs_O = list(df[col2])
    stubs_O.sort(key=Counter(stubs_O).get,reverse=False)

    num_graphs = 0

    while num_graphs < (fname_end - fname_start):
        reject_graph = False
        print num_graphs
        random.shuffle(stubs_U)
        init_cap = int(len(stubs_U)*pct_cap) # number of edges to be added initially
        init_edges = zip(stubs_O[0:init_cap],stubs_U[0:init_cap])
        R = nx.Graph()
        R.add_edges_from(init_edges)
        
        # get remaining stubs
        k_Uin,k_Oin = nx.bipartite.degrees(R,nodes_O)
        remaining_U = list((Counter(stubs_U)-Counter(k_Uin)).elements())
        remaining_O = list((Counter(stubs_O)-Counter(k_Oin)).elements())
        remaining_O.sort(key=Counter(remaining_O).get,reverse=False)

        random.shuffle(remaining_U)
        current_rej = 0
        while remaining_O and remaining_U:
            print len(remaining_O)
            prev_edgect = len(R.edges())
            R.add_edge(remaining_U[-1],remaining_O[-1])
            if prev_edgect < len(R.edges()): # if adding the edge was successful; i.e. the edge is not yet in the graph
                del remaining_U[-1]
                del remaining_O[-1]
                current_rej = 0
            else:
                random.shuffle(remaining_U)
                current_rej += 1
            if current_rej > 100 or (len(remaining_U) == 1 and current_rej > 1):
                reject_graph = True
                break

        if reject_graph == False:
            nx.write_gml(R,fname + str(num_graphs + fname_start) + ".gml")
            num_graphs += 1

def rand_sameU_randO(df, col1, col2, fname_start=0, fname_end=100):
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
            nx.write_gml(R,fname + str(len(ensemble_sample) + fname_start) + ".gml")

def get_zscores(count_from_data,fname,fname_start=0,fname_end=100,nodes_U=None,nodes_O=None):
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    num_subgraphs = len(count_from_data)
    num_rg = fname_end - fname_start
    ensemble_counts = np.zeros([num_rg,num_subgraphs],dtype=np.int64)
    i = 0
    while i < num_rg:
        nth = fname_start + i
        G = nx.read_gml(fname + str(nth) + ".gml")
        ensemble_counts[i] = bc.count_subgraphs(G, nodes_U=nodes_U, nodes_O=nodes_O)
        print nth
        i += 1
        del G

    zscores = np.zeros(num_subgraphs,dtype=np.float64)
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)

    zscores = (count_from_data - mjus) / sigmas

    return zscores