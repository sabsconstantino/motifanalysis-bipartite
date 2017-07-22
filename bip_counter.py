import networkx as nx
import numpy as np
import itertools as it
from collections import defaultdict

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

    # if list of nodes is not given, it is assumed that the nodes are labeled according to set
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0 or d['bipartite']=='u']
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1 or d['bipartite']=='o']
    else: # if it is given, the nodes are not labeled. so we label them
        nx.set_node_attributes(B, 'bipartite', dict(zip(nodes_U,['u']*len(nodes_U))))
        nx.set_node_attributes(B, 'bipartite', dict(zip(nodes_O,['o']*len(nodes_O))))

    # get numbers of nodes
    num_U = len(nodes_U)
    num_O = len(nodes_O)

    # relabel nodes to integers to save space
    B = nx.relabel_nodes(B, dict(zip(nodes_O+nodes_U,np.arange(num_O+num_U))), copy=False)

    # clear lists of node labels
    del nodes_U, nodes_O

    k_U,k_O = nx.bipartite.degrees(B,np.arange(num_O)) # get node degrees

    # https://stackoverflow.com/questions/27801945/surprising-results-with-python-timeit-counter-vs-defaultdict-vs-dict
    # initialise dictionary of pair counts
    ct_pairs_O = defaultdict(int)
    ct_pairs_U = defaultdict(int)

    # populate dictionary counting pairs of objects bought by each user
    for u in np.arange(num_O,num_O+num_U):
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            objs.sort()
            pairs_O = it.combinations(objs,2) # all possible pairs of objects bought by user u
            for p in pairs_O: #counting
                ct_pairs_O[p] += 1

    # counting o-u-o subgraphs
    subgraphs[0] = sum(ct_pairs_O.values())

    # separating pairs of objects according to count (1 / greater than 1)
    ct_pairs_O_1 = {k:v for k,v in ct_pairs_O.items() if v <= 1}
    ct_pairs_O = {k:v for k,v in ct_pairs_O.items() if v > 1}

    # counting o-u-o u and o-u-o-u subgraphs (the latter is only possible when ct_pairs_O[p] = 1)
    subgraphs[2] += sum(( num_U - (k_O[p[0]] + k_O[p[1]] - ct_pairs_O_1[p]) ) for p in ct_pairs_O_1.keys())
    subgraphs[3] = sum(( k_O[p[0]] + k_O[p[1]] - 2 ) for p in ct_pairs_O_1.keys())

    # counting o-u-o u, square, square+u, and 3-user-same-2-obj subgraphs
    subgraphs[2] += sum(( num_U - (k_O[p[0]] + k_O[p[1]] - ct_pairs_O[p]) ) for p in ct_pairs_O.keys())
    subgraphs[4] = sum(( ct_pairs_O[p]*(ct_pairs_O[p]-1) / 2 ) for p in ct_pairs_O.keys())
    subgraphs[5] = sum(( ct_pairs_O[p]*(ct_pairs_O[p]-1) / 2 )*( k_O[p[0]] + k_O[p[1]] - 2*ct_pairs_O[p] ) for p in ct_pairs_O.keys())
    subgraphs[7] = sum(( ct_pairs_O[p] * (ct_pairs_O[p]-1) * (ct_pairs_O[p]-2) / 6 ) for p in ct_pairs_O.keys())  

    # populate dictionary counting pairs of users who bought each object
    for o in np.arange(num_O):
        print o
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            usr.sort()
            pairs_U = it.combinations(usr,2) # all possible pairs of users who bought object o
            for p in pairs_U: # counting
                ct_pairs_U[p] += 1
        B.remove_node(o)

    # clear graph to clear some memory
    B.remove_nodes_from(B.nodes())

    # count u-o-u subgraphs
    subgraphs[1] = sum(ct_pairs_U.values())

    # counting square + o subgraphs
    subgraphs[6] = sum(( ct_pairs_U[p]*(ct_pairs_U[p]-1)/2 ) * ( k_U[p[0]] + k_U[p[1]] - 2*ct_pairs_U[p] ) for p in ct_pairs_U.keys())

    return subgraphs