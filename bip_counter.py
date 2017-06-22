import networkx as nx
import numpy as np
import itertools as it
import scipy.sparse as ssp

def count_motifs(B, nodes_U=None, nodes_O=None):
    """Counts motifs of a bipartite user-object graph

        Keyword arguments:
        B -- networkx bipartite graph
        nodes_U -- the first set of nodes (default None)
        nodes_O -- the second set of nodes (default None)

        Returns
        - motifs[0]: o-u-o
        - motifs[1]: u-o-u
        - motifs[2]: o-u-o-u / u-o-u-o
        - motifs[3]: square
    """
    motifs = np.zeros(4,dtype=int)

    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    k_U,k_O = nx.bipartite.degrees(B,nodes_O)

    # finding motifs 0, 2, and 3
    for u in nodes_U:
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            pairs = list(it.combinations(objs,2))
            motifs[0] += len(pairs)
            for p in pairs:
                # checking all other neighbours of u
                #uncommon_user = [j for j in B.neighbors(p[0]) if j != u]
                #uncommon_user.extend([j for j in B.neighbors(p[1]) if j != u])
                #motifs[2] += len(uncommon_user)

                # if the two objects have a common user different from u
                common_user = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                motifs[3] += len(common_user)
                motifs[2] += ( k_O[p[0]] + k_O[p[1]] - 2*(1 + len(common_user)) )

    # finding motif 1
    for o in nodes_O:
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            pairs = list(it.combinations(usr,2))
            motifs[1] += len(pairs)

    motifs[3] = motifs[3]/2

    return motifs