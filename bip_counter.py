import networkx as nx
import numpy as np
import itertools as it
from collections import defaultdict
import scipy.sparse as ssp

def count_subgraphs(B, nodes_U=None, nodes_O=None):
    """Counts subgraphs of a bipartite user-object graph. 

   Returns
   - subgraphs[0]: o-u-o
   - subgraphs[1]: u-o-u
   - subgraphs[2]: o-u-o u
   - subgraphs[3]: o-u-o-u / u-o-u-o
   - subgraphs[4]: square
   - subgraphs[5]: square + u
   - subgraphs[6]: square + o
   - subgraphs[7]: 3 users picking the same 2 objects

    Keyword arguments:
    B -- networkx bipartite graph
    nodes_U -- the first set of nodes (default None)
    nodes_O -- the second set of nodes (default None)
    """
    subgraphs = np.zeros(8,dtype=np.int64)

    # if list of nodes is not given, it is assumed that the nodes are labeled according to set
    if (nodes_U==None and nodes_O==None):
        nodes_U = [u for u,d in B.nodes_iter(data=True) if d['bipartite']==0 or d['bipartite']=='u']
        nodes_O = [o for o,d in B.nodes_iter(data=True) if d['bipartite']==1 or d['bipartite']=='o']

    # get numbers of nodes
    num_U = len(nodes_U)
    num_O = len(nodes_O)

    # relabel nodes to integers
    B = nx.relabel_nodes(B, dict(zip(nodes_U+nodes_O,np.arange(num_U+num_O))), copy=True)

    # clear lists of node labels
    del nodes_U, nodes_O

    k_U,k_O = nx.bipartite.degrees(B,np.arange(num_U,num_U+num_O)) # get node degrees

    # use sparse matrix to store counts of possible pairs of objects that were bought by each user
    row = []
    col = []
    for u in xrange(num_U):
        if k_U[u] >= 2:
            objs = B.neighbors(u)
            objs.sort()
            o1,o2 = zip(*it.combinations(objs,2)) # all possible pairs of objects bought by user u
            row.extend(o1)
            col.extend(o2)
    pairs_O = ssp.coo_matrix((np.ones(len(row)),(row,col)),shape=(num_O+num_U,num_O+num_U)).tocsr()

    # build the sparse matrices for intermediate results in other subgraph computations
    row,col = pairs_O.nonzero()
    matrix_numU = ssp.coo_matrix(([num_U]*len(row),(row,col)),shape=(num_O+num_U,num_O+num_U)).tocsr()
    data_ksum = [ k_O[row[i]] + k_O[col[i]] for i in xrange(len(row)) ]
    pairsO_ksum = ssp.coo_matrix((data_ksum,(row,col)),shape=(num_O+num_U,num_O+num_U)).tocsr()
    ones = ssp.coo_matrix((np.ones(len(row)),(row,col)),shape=(num_O+num_U,num_O+num_U)).tocsr()
    twos = ssp.coo_matrix(([2]*len(row),(row,col)),shape=(num_O+num_U,num_O+num_U)).tocsr()
    squares = (pairs_O.multiply(pairs_O-ones)) / 2
    unique_neighbors = pairsO_ksum - 2*pairs_O

    # counting subgraphs
    subgraphs[0] = pairs_O.sum()
    subgraphs[2] = (matrix_numU - (pairsO_ksum - pairs_O)).sum()
    subgraphs[3] = unique_neighbors.sum()
    subgraphs[4] = squares.sum()
    subgraphs[5] = (squares.multiply(unique_neighbors)).sum()
    subgraphs[7] = ( (pairs_O.multiply(pairs_O-ones).multiply(pairs_O-twos)) / 6 ).sum()
    del pairs_O,twos

    # use sparse matrix to store counts of possible pairs of users who bought each object
    row = []
    col = []
    for o in xrange(num_U,num_U+num_O):
        #print o - num_U
        if k_O[o] >= 2:
            usr = B.neighbors(o)
            usr.sort()
            u1,u2 = zip(*it.combinations(usr,2)) # all possible pairs of users who bought o
            row.extend(u1)
            col.extend(u2)
        B.remove_node(o)
    B.remove_nodes_from(B.nodes()) # clear graph to clear some memory

    pairs_U = ssp.coo_matrix((np.ones(len(row)),(row,col)),shape=(num_U,num_U)).tocsr()

    # count u-o-u subgraphs
    subgraphs[1] = pairs_U.sum()

    # intermediate results needed for subgraph 6 computation
    pairs_U = pairs_U.multiply(pairs_U > 1) # https://stackoverflow.com/questions/22074163/filter-values-from-a-scipy-sparse-matrix
    row,col = pairs_U.nonzero()
    data_ksum = [ k_U[row[i]] + k_U[col[i]] for i in xrange(len(row)) ]
    pairsU_ksum = ssp.coo_matrix((data_ksum,(row,col)),shape=(num_U,num_U)).tocsr()
    ones = ssp.coo_matrix((np.ones(len(row)),(row,col)),shape=(num_U,num_U)).tocsr()
    squares = (pairs_U.multiply(pairs_U-ones)) / 2
    unique_neighbors = pairsU_ksum - 2*pairs_U

    # counting square + o subgraphs
    subgraphs[6] = (squares.multiply(unique_neighbors)).sum()

    return subgraphs