import preprocessing_cumulative as pc
import bip_rand_count as brc
import pandas as pd
import numpy as np
import networkx as nx

df_mcount = pd.read_csv('subgraphdata_music.csv',index_col=0)
mfile = open('zscores_music.csv',mode='a')

#-------------------------------------------------------------------------------
# 1998-2000

#read graphs, calculate z-scores
# counts = list(df_mcount.loc['1998-2000'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_m9800_'
# out = 'random_counts/samek_m9800.csv'
# nodes_U = list(pc.df_m_00['user'].unique())
# nodes_O = list(pc.df_m_00['product'].unique())
# print 'Getting z-scores for music 98-00 data'
# zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# # write to file
# mfile.write('1998-2000,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	mfile.write(s[i] + ',')
# mfile.write(s[-1])
# mfile.write('\n')

#-------------------------------------------------------------------------------
# 1998-2003

# read graphs, calculate z-scores
# counts = list(df_mcount.loc['1998-2003'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_m9803_'
# out = 'random_counts/samek_m9803.csv'
# nodes_U = list(pc.df_m_03['user'].unique())
# nodes_O = list(pc.df_m_03['product'].unique())
# print 'Getting z-scores for music 98-03 data'
# zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# # write to file
# mfile.write('1998-2003,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	mfile.write(s[i] + ',')
# mfile.write(s[-1])
# mfile.write('\n')

#-------------------------------------------------------------------------------
# 1998-2006

#read graphs, calculcate z-scores
# fname = 'random_graphs/samek_m9806_'
# out = 'random_counts/samek_m9806.csv'
# counts = list(df_mcount.loc['1998-2006'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# nodes_U = list(pc.df_m_06['user'].unique())
# nodes_O = list(pc.df_m_06['product'].unique())
# print 'Getting z-scores for music 98-06 data'
# zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# # write to file
# mfile.write('1998-2006,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	mfile.write(s[i] + ',')
# mfile.write(s[-1])
# mfile.write('\n')

#-------------------------------------------------------------------------------
# 1998-2009

# read graphs, calculcate z-scores
# fname = 'random_graphs/samek_m9809_'
# out = 'random_counts/samek_m9809.csv'
# counts = list(df_mcount.loc['1998-2009'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# nodes_U = list(pc.df_m_09['user'].unique())
# nodes_O = list(pc.df_m_09['product'].unique())
# print 'Getting z-scores for music 98-09 data'
# zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# # write to file
# mfile.write('1998-2009,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	mfile.write(s[i] + ',')
# mfile.write(s[-1])
# mfile.write('\n')

#-------------------------------------------------------------------------------
# 1998-2012

# read graphs, calculcate z-scores
fname = 'random_graphs/samek_m9812_'
out = 'random_counts/samek_m9812.csv'
counts = list(df_mcount.loc['1998-2012'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
nodes_U = list(pc.df_m_12['user'].unique())
nodes_O = list(pc.df_m_12['product'].unique())
print 'Getting z-scores for music 98-12 data'
zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# write to file
mfile.write('1998-2012,same_degrees,')
s = str(zscores)
s = s.replace('[','')
s = s.replace(']','')
s = s.split()
for i in np.arange(len(s)-1):
	mfile.write(s[i] + ',')
mfile.write(s[-1])
mfile.write('\n')

#-------------------------------------------------------------------------------
# 1998-2014

# read graphs, calculcate z-scores
fname = 'random_graphs/samek_m9814_'
out = 'random_counts/samek_m9814.csv'
counts = list(df_mcount.loc['1998-2014'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
nodes_U = list(pc.df_m_14['user'].unique())
nodes_O = list(pc.df_m_14['product'].unique())
print 'Getting z-scores for music 98-14 data'
zscores = brc.get_zscores(counts,fname,outfile=out,nodes_U=nodes_U,nodes_O=nodes_O) 

# write to file
mfile.write('1998-2014,same_degrees,')
s = str(zscores)
s = s.replace('[','')
s = s.replace(']','')
s = s.split()
for i in np.arange(len(s)-1):
	mfile.write(s[i] + ',')
mfile.write(s[-1])
mfile.write('\n')
mfile.close()