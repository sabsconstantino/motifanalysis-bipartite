import preprocessing_cumulative as pc
import bip_rand_count as brc
import pandas as pd
import numpy as np
import networkx as nx

df_vgcount = pd.read_csv('subgraphdata_videogames.csv',index_col=0)
vgfile = open('zscores_videogames.csv',mode='a')

#-------------------------------------------------------------------------------
# 1997-2000

# read graphs, calculate z-scores
# counts = list(df_vgcount.loc['1997-2000'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_vg9700_'
# out = 'random_counts/samek_vg9700.csv'
# # nodes_U = list(pc.df_vg_00['user'].unique())
# # nodes_O = list(pc.df_vg_00['product'].unique())
# print 'Getting z-scores for video game 97-00 data'
# zscores = brc.get_zscores(counts,fname,outfile=out) 

# # write to file
# vgfile.write('1997-2000,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')

#-------------------------------------------------------------------------------
# 1997-2003

# counts = list(df_vgcount.loc['1997-2003'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_vg9703_'
# out = 'random_counts/samek_vg9703.csv'
# # nodes_U = list(pc.df_vg_03['user'].unique())
# # nodes_O = list(pc.df_vg_03['product'].unique())
# print 'Getting z-scores for video game 97-03 data'
# zscores = brc.get_zscores(counts,fname,outfile=out) 

# # write to file
# vgfile.write('1997-2003,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')

#-------------------------------------------------------------------------------
# 1997-2006

# counts = list(df_vgcount.loc['1997-2006'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_vg9706_'
# out = 'random_counts/samek_vg9706.csv'
# # nodes_U = list(pc.df_vg_06['user'].unique())
# # nodes_O = list(pc.df_vg_06['product'].unique())
# print 'Getting z-scores for video game 97-06 data'
# zscores = brc.get_zscores(counts,fname,outfile=out) 

# # write to file
# vgfile.write('1997-2006,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')
# vgfile.close()

#-------------------------------------------------------------------------------
# 1997-2009

# counts = list(df_vgcount.loc['1997-2009'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_vg9709_'
# out = 'random_counts/samek_vg9709.csv'
# print 'Getting z-scores for video game 97-09 data'
# zscores = brc.get_zscores(counts,fname,outfile=out) 


# # write to file
# vgfile.write('1997-2009,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')

#-------------------------------------------------------------------------------
# 1997-2012

# counts = list(df_vgcount.loc['1997-2012'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
# fname = 'random_graphs/samek_vg9712_'
# out = 'random_counts/samek_vg9712.csv'
# # nodes_U = list(pc.df_vg_12['user'].unique())
# # nodes_O = list(pc.df_vg_12['product'].unique())
# print 'Getting z-scores for video game 97-12 data'
# zscores = brc.get_zscores(counts,fname,outfile=out) 

# # write to file
# vgfile.write('1997-2012,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')
# vgfile.close()

#-------------------------------------------------------------------------------
# 1997-2014

counts = list(df_vgcount.loc['1997-2014x'][['subgraph_0','subgraph_1','subgraph_2','subgraph_3','subgraph_4','subgraph_5','subgraph_6','subgraph_7']])
fname = 'random_graphs/samek_vg9714x_'
out = 'random_counts/samek_vg9714x_8999.csv'
print 'Getting counts for video game 97-14x data'
counts = brc.get_counts(infile=fname,outfile=out,infile_start=89,infile_end=100) 

# write to file
# vgfile.write('1997-2014x,same_degrees,')
# s = str(zscores)
# s = s.replace('[','')
# s = s.replace(']','')
# s = s.split()
# for i in np.arange(len(s)-1):
# 	vgfile.write(s[i] + ',')
# vgfile.write(s[-1])
# vgfile.write('\n')
# vgfile.close()