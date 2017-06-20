import networkx as nx
import preprocessing_cumulative as pc
import preprocessing as pp
import plfit
import plplot

'''This module is for generating the degree sequences for cumulative data
'''

#--------------------------------------------------------------------------
# Music data, cumulative

B = nx.from_pandas_dataframe(pc.df_m_00,source='user',target='product')
nodes_O = list(pc.df_m_00['product'].unique())
m00_kU,m00_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_m_03,source='user',target='product')
nodes_O = list(pc.df_m_03['product'].unique())
m03_kU,m03_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_m_06,source='user',target='product')
nodes_O = list(pc.df_m_06['product'].unique())
m06_kU,m06_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_m_09,source='user',target='product')
nodes_O = list(pc.df_m_09['product'].unique())
m09_kU,m09_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_m_12,source='user',target='product')
nodes_O = list(pc.df_m_12['product'].unique())
m12_kU,m12_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_m_14,source='user',target='product')
nodes_O = list(pc.df_m_14['product'].unique())
m14_kU,m14_kO = nx.bipartite.degrees(B,nodes_O)


#--------------------------------------------------------------------------
# Video game data, cumulative

B = nx.from_pandas_dataframe(pc.df_vg_00,source='user',target='product')
nodes_O = list(pc.df_vg_00['product'].unique())
vg00_kU,vg00_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_03,source='user',target='product')
nodes_O = list(pc.df_vg_03['product'].unique())
vg03_kU,vg03_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_06,source='user',target='product')
nodes_O = list(pc.df_vg_06['product'].unique())
vg06_kU,vg06_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_09,source='user',target='product')
nodes_O = list(pc.df_vg_09['product'].unique())
vg09_kU,vg09_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_12,source='user',target='product')
nodes_O = list(pc.df_vg_12['product'].unique())
vg12_kU,vg12_kO = nx.bipartite.degrees(B,nodes_O)

B = nx.from_pandas_dataframe(pc.df_vg_14,source='user',target='product')
nodes_O = list(pc.df_vg_14['product'].unique())
vg14_kU,vg14_kO = nx.bipartite.degrees(B,nodes_O)