import networkx as nx
import preprocessing_cumulative as pc
import preprocessing as pp
import plfit
import plplot

# This module is for fitting power laws to the music and video game data.
# plfit and plplot can be found at: 
#   http://tuvalu.santafe.edu/~aaronc/powerlaws/

#--------------------------------------------------------------------------
# Music data, cumulative

B = nx.from_pandas_dataframe(pc.df_m_00,source='user',target='product')
nodes_U = list(pc.df_m_00['user'].unique())
nodes_O = list(pc.df_m_00['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9800 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.78, 2, -3683.9248650772533], [2.16, 6, -3216.0023338559513]]

B = nx.from_pandas_dataframe(pc.df_m_03,source='user',target='product')
nodes_U = list(pc.df_m_03['user'].unique())
nodes_O = list(pc.df_m_03['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9803 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.62, 2, -12921.788125887044], [2.21, 21, -3440.50732401333]]

B = nx.from_pandas_dataframe(pc.df_m_06,source='user',target='product')
nodes_U = list(pc.df_m_06['user'].unique())
nodes_O = list(pc.df_m_06['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9806 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.55, 2, -24975.374459847328], [2.34, 47, -3254.6804231527362]]

B = nx.from_pandas_dataframe(pc.df_m_09,source='user',target='product')
nodes_U = list(pc.df_m_09['user'].unique())
nodes_O = list(pc.df_m_09['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9809 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.53, 3, -20548.985439634303], [2.27, 37, -5503.491837336332]]

B = nx.from_pandas_dataframe(pc.df_m_12,source='user',target='product')
nodes_U = list(pc.df_m_12['user'].unique())
nodes_O = list(pc.df_m_12['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9812 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.67, 3, -37915.7913950638], [1.91, 3, -46184.87367810719]]

B = nx.from_pandas_dataframe(pc.df_m_14,source='user',target='product')
nodes_U = list(pc.df_m_14['user'].unique())
nodes_O = list(pc.df_m_14['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_m9814 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.56, 1, -420474.54408050433], [2.1, 4, -86624.02922341874]]

#--------------------------------------------------------------------------
# Video game data, cumulative

B = nx.from_pandas_dataframe(pc.df_vg_02,source='user',target='product')
nodes_U = list(pc.df_vg_02['user'].unique())
nodes_O = list(pc.df_vg_02['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_vg9802 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.84, 1, -25697.55514074794], [3.1, 85, -444.73374409778796]]

B = nx.from_pandas_dataframe(pc.df_vg_05,source='user',target='product')
nodes_U = list(pc.df_vg_05['user'].unique())
nodes_O = list(pc.df_vg_05['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_vg9805 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.56, 2, -22985.52335387547], [2.59, 50, -2101.779055639176]]

B = nx.from_pandas_dataframe(pc.df_vg_08,source='user',target='product')
nodes_U = list(pc.df_vg_08['user'].unique())
nodes_O = list(pc.df_vg_08['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_vg9808 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.66, 2, -41875.97497871601], [3.01, 118, -1263.8594570209102]]

B = nx.from_pandas_dataframe(pc.df_vg_11,source='user',target='product')
nodes_U = list(pc.df_vg_11['user'].unique())
nodes_O = list(pc.df_vg_11['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_vg9811 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.73, 2, -83805.42448046157], [2.79, 130, -2696.6750762703605]]

B = nx.from_pandas_dataframe(pc.df_vg_14,source='user',target='product')
nodes_U = list(pc.df_vg_14['user'].unique())
nodes_O = list(pc.df_vg_14['product'].unique())
k_U,k_O = nx.bipartite.degrees(B,nodes_O)

pl_vg9814 = [plfit.plfit(k_U.values()), plfit.plfit(k_O.values())]
#[[2.96, 8, -22537.716892050834], [2.83, 348, -2317.5839814877613]]