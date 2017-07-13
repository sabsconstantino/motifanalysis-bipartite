import networkx as nx
import numpy as np
import itertools as it
import scipy.sparse as ssp
from collections import Counter

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
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    k_U,k_O = nx.bipartite.degrees(B,nodes_O)
    num_U = len(nodes_U)

    pairs_O = []
    for u in nodes_U:
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            pairs_O.extend(list(it.combinations(objs,2)))

    pairs_U = []
    for o in nodes_O:
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            pairs_U.extend(list(it.combinations(usr,2)))

    pairs_U.sort(key = lambda x: x[0])
    pairs_O.sort(key = lambda x: x[0])

    ct_pairs_U = Counter(pairs_U)
    ct_pairs_O = Counter(pairs_O)

    subgraphs[0] = len(pairs_O)
    subgraphs[1] = len(pairs_U)

    for p in ct_pairs_O.keys():
        subgraphs[2] += num_U - ( k_O[p[0]] + k_O[p[1]] - ct_pairs_O[p] )
        subgraphs[3] += ct_pairs_O[p]*( k_O[p[0]] + k_O[p[1]] - 2 )
        if ct_pairs_O[p] > 1:
            squares = ct_pairs_O[p]*(ct_pairs_O[p]-1)/2
            subgraphs[4] += squares
            subgraphs[5] += squares*len(set(B.neighbors(p[0])).symmetric_difference(set(B.neighbors(p[1]))))
            subgraphs[7] += ct_pairs_O[p]*(ct_pairs_O[p]-1)*(ct_pairs_O[p]-2) / 6

    for p in ct_pairs_U.keys():
        if ct_pairs_U[p] > 1:
            squares = ct_pairs_U[p]*(ct_pairs_U[p]-1)/2
            subgraphs[6] += squares*len(set(B.neighbors(p[0])).symmetric_difference(set(B.neighbors(p[1]))))
            

    subgraphs[3] -= 3*subgraphs[4]

    # # finding subgraphs 0, 2, and 3
    # for u in nodes_U:
    #     if k_U[u] >= 2:
    #         objs = B.neighbors(u)
    #         pairs = list(it.combinations(objs,2))
    #         subgraphs[0] += len(pairs)
    #         for p in pairs:
    #             subgraphs[3] += ( k_O[p[0]] + k_O[p[1]] - 2 )
    #             # if the pairs of objects have a common user other than the current one
    #             common_user = len(set(B.neighbors(p[0])).intersection(set(B.neighbors(p[1]))))
    #             subgraphs[4] += (common_user - 1)
    #             if common_user > 1:
    #                 subgraphs[5] += ( k_O[p[0]] + k_O[p[1]] - 4 )
    #                 subgraphs[7] += common_user*(common_user-1)*(common_user-2) / 6
    #             subgraphs[2] += num_U - ( k_O[p[0]] + k_O[p[1]] - common_user ) 

    # # finding motif 1
    # for o in nodes_O:
    #     if k_O[o] >= 2:
    #         usr = B.neighbors(o)
    #         pairs = list(it.combinations(usr,2))
    #         subgraphs[1] += len(pairs)
    #         for p in pairs:
    #             common_obj = len(set(B.neighbors(p[0])).intersection(set(B.neighbors(p[1]))))
    #             if common_obj > 1:
    #                 subgraphs[6] += ( k_U[p[0]] + k_U[p[1]] - 4 )

    # subgraphs[4] = subgraphs[4]/2
    # subgraphs[3] = subgraphs[3] - 3*subgraphs[4]
    # subgraphs[5] = subgraphs[5]/2
    # subgraphs[6] = subgraphs[6]/2
    # subgraphs[7] = subgraphs[7]/3

    return subgraphs