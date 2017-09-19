import networkx as nx
from collections import Counter
import bip_counter as bc
import numpy as np
from datetime import datetime as dt
import pandas as pd

"""This module is generating samples from ensembles of random graphs, and for computing the zscores of the subgraph counts.
"""

def rand_samedegrees(df, col1, col2, outfile, outfile_start=0, outfile_end=100):
    """Generates (outfile_end-outfile_start) random graphs with the same degrees as the bipartite network represented by df. Outputs compressed gml files.

    Keyword arguments:
    df -- pandas dataframe containing network data
    col1 -- column name of bipartite node set U
    col2 -- column name of bipartite node set O
    outfile -- output file prefix
    outfile_start -- starting number of filename (default 0)
    outfile_end -- ending number of filename (default 100)
    """
    stubs_U = list(df[col1])
    stubs_O = list(df[col2])

    k_O = Counter(stubs_O).most_common() # list of node-degree tuples (o, k_o)
    stubs_O1 = [o[0] for o in k_O if o[1]==1] # get all objects with degree 1
    k_O = [o for o in k_O if o[1]!=1] # all other objects
    num_graphs = 0

    while num_graphs < (outfile_end - outfile_start):
        print num_graphs
        k_U = Counter(stubs_U)

        R = nx.Graph()
        R.add_nodes_from(set(stubs_U), bipartite='u')
        R.add_nodes_from(set(stubs_O), bipartite='o')
        edges = []

        # perform stub matching on all objects with degree greater than 1
        for o in k_O:
            users = np.random.choice(k_U.keys(),o[1],replace=False) # choose k_o users without replacement
            edges = zip( [o[0]]*o[1], users )
            R.add_edges_from(edges)
            # removal of stubs from users
            for u in users:
                if k_U[u] == 1:
                    del k_U[u]
                else:
                    k_U[u] = k_U[u]-1

        # perform stub matching on all objects with degree 1
        stubs_U_rem = list(k_U.elements())
        np.random.shuffle(stubs_U_rem)
        R.add_edges_from(zip(stubs_O1,stubs_U_rem))

        nx.write_gml(R,outfile + str(num_graphs + outfile_start) + ".gml.gz")
        num_graphs += 1

def rand_randomobj(df, col1, col2, outfile, outfile_start=0, outfile_end=100):
    """Generates (outfile_end-outfile_start) random graphs with the same degree of U (col1) and randomized degrees of O (col2; uniform distribution). Outputs compressed gml files.

    Keyword arguments:
    df -- pandas dataframe containing network data
    col1 -- column name of bipartite node set U
    col2 -- column name of bipartite node set O
    outfile -- output file prefix
    outfile_start -- starting number of filename (default 0)
    outfile_end -- ending number of filename (default 100)
    """
    nodes_U = list(df[col1].unique())
    nodes_O = list(df[col2].unique())
    num_O = len(nodes_O)
    
    num_graphs = 0

    while num_graphs < (outfile_end - outfile_start):
        print num_graphs
        R = nx.Graph()
        R.add_nodes_from(nodes_O, bipartite='o')
        R.add_nodes_from(nodes_U, bipartite='u')

        # choose random objects to pair with users
        stubs_U = list(df[col1])
        stubs_O = np.random.choice(nodes_O, len(stubs_U), replace=True)
        edges = zip(stubs_U, stubs_O)
        R.add_edges_from(edges)

        # get remaining stubs (in case some edges were rejected from first round)
        nodes_Uin = [u for u,d in R.nodes(data=True) if d['bipartite']=='u']
        stubs_Uin = Counter(nx.bipartite.degrees(R,nodes_Uin)[1])
        k_U = Counter(stubs_U) - stubs_Uin # counter of remaining stubs from U

        # pair remaining stubs
        for u in k_U.keys():
            poss_O = set(nodes_O) - set(R.neighbors(u)) # list of objects we can possibly choose from
            objects = np.random.choice(list(poss_O), k_U[u], replace=False)
            R.add_edges_from( zip( [u]*k_U[u], objects ) )

        nx.write_gml(R,outfile + str(num_graphs + outfile_start) + ".gml.gz")
        num_graphs += 1

def rand_randomuser(df, col1, col2, outfile, outfile_start=0, outfile_end=100):
    """Generates (outfile_end-outfile_start) random graphs with randomized degrees of U (col1) and same degrees of O (col2; uniform distribution). Outputs compressed gml files.

    Keyword arguments:
    df -- pandas dataframe containing network data
    col1 -- column name of bipartite node set U
    col2 -- column name of bipartite node set O
    outfile -- output file prefix
    outfile_start -- starting number of filename (default 0)
    outfile_end -- ending number of filename (default 100)
    """
    nodes_U = list(df[col1].unique())
    nodes_O = list(df[col2].unique())
    num_O = len(nodes_O)
    
    num_graphs = 0

    while num_graphs < (outfile_end - outfile_start):
        print num_graphs
        R = nx.Graph()
        R.add_nodes_from(nodes_O, bipartite='o')
        R.add_nodes_from(nodes_U, bipartite='u')

        # choose random users to pair with objects
        stubs_O = list(df[col2])
        stubs_U = np.random.choice(nodes_U, len(stubs_O), replace=True)
        edges = zip(stubs_U, stubs_O)
        R.add_edges_from(edges)

        # get remaining stubs (in case some edges were rejected from first round)
        nodes_Oin = [o for o,d in R.nodes(data=True) if d['bipartite']=='o']
        stubs_Oin = Counter(nx.bipartite.degrees(R,nodes_Oin)[1])
        k_O = Counter(stubs_O) - stubs_Oin # counter of remaining stubs from U

        # pair remaining stubs
        for o in k_O.keys():
            poss_U = set(nodes_U) - set(R.neighbors(o)) # list of objects we can possibly choose from
            users = np.random.choice(list(poss_U), k_O[o], replace=False)
            R.add_edges_from( zip( [o]*k_O[o], users ) )

        nx.write_gml(R,outfile + str(num_graphs + outfile_start) + ".gml.gz")
        num_graphs += 1

def get_zscores(count_from_data, infile):
    """Calculates the zscore per subgraph of the actual data vs. the random graphs.

    Keyword arguments:
    count_from_data -- an array containing subgraph counts of the actual data
    infile -- name of file containing subgraph counts of each random graph
    """
    num_subgraphs = len(count_from_data)
    zscores = np.zeros(num_subgraphs,dtype=np.float64)
    ensemble_counts = pd.read_csv(infile, header=0).as_matrix()
    mjus = np.mean(ensemble_counts,axis=0)
    sigmas = np.std(ensemble_counts,axis=0)
    zscores = (count_from_data - mjus) / sigmas

    return zscores


def get_counts(outfile,infile,is_compressed=True,infile_start=0,infile_end=100,nodes_U=None,nodes_O=None):
    """Counts the subgraphs of the random graphs.

    Keyword arguments:
    outfile -- file where the subgraph counts of the random graphs are to be written
    outfile -- filename prefix of random graphs to be counted
    is_compressed -- whether the random graph gml files are compressed (default True)
    infile_start -- starting number of random graph filename (default 0)
    infile_end -- ending number of random graph filename (default 100)
    nodes_U -- unique list or set of nodes corresponding to bipartite node set U. This is necessary when there is no 'bipartite' node attribute in the random graph data. (default None)
    nodes_O -- unique list or set of nodes corresponding to bipartite node set O. This is necessary when there is no 'bipartite' node attribute in the random graph data. (default None)
    """
    num_subgraphs = 8
    num_rg = infile_end - infile_start
    ensemble_counts = np.zeros([num_rg,num_subgraphs],dtype=np.int64)
    i = 0
    while i < num_rg:
        nth = infile_start + i
        if not is_compressed:
            G = nx.read_gml(infile + str(nth) + ".gml")
        else:
            G = nx.read_gml(infile + str(nth) + ".gml.gz")
        ensemble_counts[i] = bc.count_subgraphs(G, nodes_U=nodes_U, nodes_O=nodes_O)
        print str(nth) +' '+ str(dt.now())
        i += 1
        del G

    h = ''
    for i in np.arange(num_subgraphs-1):
        h += 'subgraph_' + str(i) + ','
    h += 'subgraph_' + str(num_subgraphs-1)
    np.savetxt(outfile, ensemble_counts, header=h, delimiter=',')