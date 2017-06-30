import networkx as nx
import numpy as np
import itertools as it
import scipy.sparse as ssp

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

    # finding subgraphs 0, 2, and 3
    for u in nodes_U:
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            pairs = list(it.combinations(objs,2))
            subgraphs[0] += len(pairs)
            for p in pairs:
                subgraphs[3] += ( k_O[p[0]] + k_O[p[1]] - 2 )
                # if the pairs of objects have a common user other than the current one
                common_user = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                subgraphs[4] += len(common_user)
                if common_user:
                    subgraphs[5] += ( k_O[p[0]] + k_O[p[1]] - 4 )
                    subgraphs[7] += (len(common_user) + 1)*len(common_user)*(len(common_user) - 1) / 6
                subgraphs[2] += num_U - ( k_O[p[0]] + k_O[p[1]] - 1 - len(common_user) ) 

    # finding motif 1
    for o in nodes_O:
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            pairs = list(it.combinations(usr,2))
            subgraphs[1] += len(pairs)
            for p in pairs:
                common_obj = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                if common_obj:
                    subgraphs[6] += ( k_U[p[0]] + k_U[p[1]] - 4 )

    subgraphs[4] = subgraphs[4]/2
    subgraphs[3] = subgraphs[3] - 3*subgraphs[4]
    subgraphs[5] = subgraphs[5]/2
    subgraphs[6] = subgraphs[6]/2
    subgraphs[7] = subgraphs[7]/3

    return subgraphs