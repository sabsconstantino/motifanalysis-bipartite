import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''This module is for plotting the zscores of subgraph types 2 to 7, for every subset of music data.

Reference:
[1] "statistics example code: boxplot_color_demo.py", https://matplotlib.org/examples/statistics/boxplot_color_demo.html.
'''

df_a = pd.read_csv('subgraphdata_music.csv')
df_a = df_a.drop(['years','K','num_U','num_O','avg_kO','avg_kU','subgraph_0','subgraph_1'],axis=1)
S = df_a.as_matrix() # rows: years, cols: subgraphs

df_k00 = pd.read_csv('random_counts/samek_m9800.csv')
df_k00 = df_k00.drop(['# subgraph_0','subgraph_1'],axis=1)
df_k03 = pd.read_csv('random_counts/samek_m9803.csv')
df_k03 = df_k03.drop(['# subgraph_0','subgraph_1'],axis=1)
df_k06 = pd.read_csv('random_counts/samek_m9806.csv')
df_k06 = df_k06.drop(['# subgraph_0','subgraph_1'],axis=1)
df_k09 = pd.read_csv('random_counts/samek_m9809.csv')
df_k09 = df_k09.drop(['# subgraph_0','subgraph_1'],axis=1)
df_k12 = pd.read_csv('random_counts/samek_m9812.csv')
df_k12 = df_k12.drop(['# subgraph_0','subgraph_1'],axis=1)
df_k14 = pd.read_csv('random_counts/samek_m9814.csv')
df_k14 = df_k14.drop(['# subgraph_0','subgraph_1'],axis=1)

R_s2 = np.array([df_k00['subgraph_2'],df_k03['subgraph_2'],df_k06['subgraph_2'],df_k09['subgraph_2'],df_k12['subgraph_2'],df_k14['subgraph_2']]).transpose()
R_s3 = np.array([df_k00['subgraph_3'],df_k03['subgraph_3'],df_k06['subgraph_3'],df_k09['subgraph_3'],df_k12['subgraph_3'],df_k14['subgraph_3']]).transpose()
R_s4 = np.array([df_k00['subgraph_4'],df_k03['subgraph_4'],df_k06['subgraph_4'],df_k09['subgraph_4'],df_k12['subgraph_4'],df_k14['subgraph_4']]).transpose()
R_s5 = np.array([df_k00['subgraph_5'],df_k03['subgraph_5'],df_k06['subgraph_5'],df_k09['subgraph_5'],df_k12['subgraph_5'],df_k14['subgraph_5']]).transpose()
R_s6 = np.array([df_k00['subgraph_6'],df_k03['subgraph_6'],df_k06['subgraph_6'],df_k09['subgraph_6'],df_k12['subgraph_6'],df_k14['subgraph_6']]).transpose()
R_s7 = np.array([df_k00['subgraph_7'],df_k03['subgraph_7'],df_k06['subgraph_7'],df_k09['subgraph_7'],df_k12['subgraph_7'],df_k14['subgraph_7']]).transpose()

Z_s2 = (S[:,0]-R_s2)/np.std(R_s2,axis=0)
Z_s3 = (S[:,1]-R_s3)/np.std(R_s3,axis=0)
Z_s4 = (S[:,2]-R_s4)/np.std(R_s4,axis=0)
Z_s5 = (S[:,3]-R_s5)/np.std(R_s5,axis=0)
Z_s6 = (S[:,4]-R_s6)/np.std(R_s6,axis=0)
Z_s7 = (S[:,5]-R_s7)/np.std(R_s7,axis=0)

# Creating boxplots for each subset [1]
fig,axes = plt.subplots(nrows=3, ncols=2, figsize=(18, 18))
bplot2 = axes[0,0].boxplot(Z_s2,vert=True)
bplot3 = axes[1,0].boxplot(Z_s3,vert=True)
bplot4 = axes[2,0].boxplot(Z_s4,vert=True)
bplot5 = axes[0,1].boxplot(Z_s5,vert=True)
bplot6 = axes[1,1].boxplot(Z_s6,vert=True)
bplot7 = axes[2,1].boxplot(Z_s7,vert=True)

axes[0,0].set_title('Subgraph Type 2 Z-Scores')
axes[1,0].set_title('Subgraph Type 3 Z-Scores')
axes[2,0].set_title('Subgraph Type 4 Z-Scores')
axes[0,1].set_title('Subgraph Type 5 Z-Scores')
axes[1,1].set_title('Subgraph Type 6 Z-Scores')
axes[2,1].set_title('Subgraph Type 7 Z-Scores')

# adding horizontal grid lines
for ax in axes.flatten():
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(7)],)
    #ax.set_xlabel('Subset')
    ax.set_ylabel('Z-score')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(7)],
         xticklabels=['music_00', 'music_03', 'music_06', 'music_09', 'music_12', 'music_14'])

plt.savefig('plots/zscores_m_samek.png')
#plt.show()