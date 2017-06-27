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
        - subgraphs[2]: o-u-o-u / u-o-u-o
        - subgraphs[3]: square
        - subgraphs[4]: square + u
        - subgraphs[5]: square + o
        - subgraphs[6]: "complete" 5 nodes (3 usr + 2 obj)
        - subgraphs[7]: "complete" 5 nodes (2 usr + 3 obj)
    """
    subgraphs = np.zeros(8,dtype=int)

    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    k_U,k_O = nx.bipartite.degrees(B,nodes_O)

    # finding subgraphs 0, 2, and 3
    for u in nodes_U:
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            pairs = list(it.combinations(objs,2))
            subgraphs[0] += len(pairs)
            for p in pairs:               
                subgraphs[2] += ( k_O[p[0]] + k_O[p[1]] - 2 )
                # if the pairs of objects have a common user other than the current one
                common_user = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                subgraphs[3] += len(common_user)
                if common_user:
                    subgraphs[4] += ( k_O[p[0]] + k_O[p[1]] - 4 )

    # finding motif 1
    for o in nodes_O:
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            pairs = list(it.combinations(usr,2))
            subgraphs[1] += len(pairs)
            for p in pairs:
                common_obj = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                if common_obj:
                    subgraphs[5] += ( k_U[p[0]] + k_[p[1]] - 4 )


    subgraphs[3] = subgraphs[3]/2
    subgraphs[2] = subgraphs[2] - 3*subgraphs[3]
    subgraphs[4] = subgraphs[4]/2
    subgraphs[5] = subgraphs[5]/2

    return subgraphs