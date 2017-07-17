import networkx as nx
import numpy as np
import itertools as it
import scipy.sparse as ssp
from collections import Counter, defaultdict
from datetime import datetime as dt

def count_subgraphs(B, nodes_U=None, nodes_O=None):
    """Counts subgraphs of a bipartite user-object graph

        Keyword arguments:
        B -- networkx bipartite graph
        nodes_U -- the first set of nodes (default None)
        nodes_O -- the second set of nodes (default None)

        Returns
        - subgraphs[0]: o-u-o
        - subgraphs[1]: u-o-u
        - subgraphs[2]: o-u-o u
        - subgraphs[3]: o-u-o-u / u-o-u-o
        - subgraphs[4]: square
        - subgraphs[5]: square + u
        - subgraphs[6]: square + o
        - subgraphs[7]: 3 users picking the same 2 objects
    """
    subgraphs = np.zeros(8,dtype=np.int64)

    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0 or d['bipartite']=='u']
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1 or d['bipartite']=='o']

    k_U,k_O = nx.bipartite.degrees(B,nodes_O)
    num_U = len(nodes_U)

    nodes_U.sort(key=k_U.get, reverse=False)
    nodes_O.sort(key=k_O.get, reverse=False)

    # https://stackoverflow.com/questions/27801945/surprising-results-with-python-timeit-counter-vs-defaultdict-vs-dict
    ct_pairs_O = defaultdict(int)
    ct_pairs_U = defaultdict(int)

    #print 'hey ' + str(dt.now()) 
    while nodes_U:
        u = nodes_U.pop()
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            objs.sort()
            pairs_O = it.combinations(objs,2)
            for p in pairs_O:
                ct_pairs_O[p] += 1

    #print 'ho ' + str(dt.now())
    while nodes_O:
        #print len(nodes_O)
        o = nodes_O.pop()
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            usr.sort()
            pairs_U = it.combinations(usr,2)
            for p in pairs_U:
                ct_pairs_U[p] += 1

    subgraphs[0] = sum(ct_pairs_O.values())
    subgraphs[1] = sum(ct_pairs_U.values())

    #print 'are we there yet ' + str(dt.now())
    for p in ct_pairs_O.keys():
        #print len(ct_pairs_O.keys())
        subgraphs[2] += num_U - ( k_O[p[0]] + k_O[p[1]] - ct_pairs_O[p] )
        if ct_pairs_O[p] <= 1: # if there are more than one users who bought the two objects p
            subgraphs[3] += k_O[p[0]] + k_O[p[1]] - 2 
        else:
            squares = ct_pairs_O[p]*(ct_pairs_O[p]-1)/2
            subgraphs[4] += squares
            subgraphs[5] += squares*( k_O[p[0]] + k_O[p[1]] - 2*ct_pairs_O[p] )
            subgraphs[7] += ct_pairs_O[p]*(ct_pairs_O[p]-1)*(ct_pairs_O[p]-2) / 6
        del ct_pairs_O[p]

    #print 'almost there ' + str(dt.now())
    for p in ct_pairs_U.keys():
        #print len(ct_pairs_U.keys())
        if ct_pairs_U[p] > 1:
            squares = ct_pairs_U[p]*(ct_pairs_U[p]-1)/2
            subgraphs[6] += squares*( k_U[p[0]] + k_U[p[1]] - 2*ct_pairs_U[p] )
        del ct_pairs_U[p]

    return subgraphs