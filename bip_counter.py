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
        - motifs[2]: o-u-o u
        - motifs[3]: u-o-u o
        - motifs[4]: square
        - motifs[5]: o-u-o-u / u-o-u-o
    """
    motifs = np.zeros(6)

    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0]
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1]

    num_U = len(nodes_U)
    num_O = len(nodes_O)

    nodes_U.sort()
    nodes_O.sort()

    Ba = nx.adjacency_matrix(B,nodes_U+nodes_O)
    Ba = ssp.dok_matrix(Ba)

    k_U,k_O = nx.bipartite.degrees(B,nodes_O)

    # map nodes_U to integers (in case the node names are strings or some other type)
    # the integers are needed for checking the adjacency matrix
    nodes_U = dict(zip(nodes_U, np.arange(num_U)))
    nodes_O = dict(zip(nodes_O, np.arange(num_U,num_U+num_O)))

    # finding motifs 0, 2, and 4
    for u in nodes_U.keys():
    	print 'user ' + str(u) + ' ' + str(nodes_U[u])
        if k_U[u] >= 2:
            objs = [o for o in nodes_O.keys() if Ba[nodes_U[u],nodes_O[o]]==1]
            pairs = list(it.combinations(objs,2))
            motifs[0] += len(pairs)
            for p in pairs:
                motifs[2] += num_U - (k_O[p[0]] + k_O[p[1]] - 2)
                # if the two objects have a common user different from u
                common_user = [j for j in B.neighbors(p[0]) if j in B.neighbors(p[1]) and j != u]
                motifs[4] += len(common_user)

    # finding motifs 1, 3, and 5
    for o in nodes_O.keys():
    	print 'object ' + str(o) + ' ' + str(nodes_O[o])
        if k_O[o] >= 2:
            usr = [u for u in nodes_U.keys() if Ba[nodes_U[u],nodes_O[o]]==1]
            pairs = list(it.combinations(usr,2))
            motifs[1] += len(pairs)
            for p in pairs:
                motifs[3] += num_O - (k_U[p[0]] + k_U[p[1]] - 2)
                motifs[5] += k_U[p[0]] + k_U[p[1]] - 2

    motifs[2] -= motifs[0]
    motifs[3] -= motifs[1]
    motifs[4] = motifs[4]/2
    motifs[5] = motifs[5]/2 - motifs[4]

    return motifs