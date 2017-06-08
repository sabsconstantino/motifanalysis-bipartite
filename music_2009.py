import networkx as nx
import preprocessing as pp
import numpy as np
import bip_counter as bc

B = nx.Graph();

B = nx.from_pandas_dataframe(pp.df_music_HR_09,source='user',target='product')

nodes_U = list(pp.df_music_HR_09['user'].unique())
nodes_O = list(pp.df_music_HR_09['product'].unique())

motifs = bc.count_motifs(B,nodes_U=nodes_U,nodes_O=nodes_O)