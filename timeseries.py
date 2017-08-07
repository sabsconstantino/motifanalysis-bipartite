import matplotlib.pyplot as plt
import pandas as pd

yr = [1997,2000,2003,2006,2009,2012,2014]

dfm = pd.read_csv('subgraphdata_music.csv',header=0)

m_K = [0]
m_K.extend(list(dfm['K']))

m_numU = [0]
m_numU.extend(list(dfm['num_U']))

m_numO = [0]
m_numO.extend(list(dfm['num_O']))

m_avg_kU = [0]
m_avg_kU.extend(list(dfm['avg_kU']))

m_avg_kO = [0]
m_avg_kO.extend(list(dfm['avg_kO']))

plt.figure()
plt.plot(yr, m_K,c='g')
plt.xlabel("Year")
plt.ylabel("K")
plt.savefig('plots/music_ts_edges.png')

plt.figure()
plt.plot(yr, m_numU,c='b')
plt.plot(yr, m_numO,c='r')
plt.xlabel("Year")
plt.ylabel("Nodes")
plt.savefig('plots/music_ts_nodes.png')

plt.figure()
plt.plot(yr, m_avg_kU,c='b')
plt.plot(yr, m_avg_kO,c='r')
plt.xlabel("Year")
plt.ylabel("Avg. degree")
plt.savefig('plots/music_ts_avg.png')

# --------------------------------------------------------------

dfvg = pd.read_csv('subgraphdata_videogames.csv',header=0)[0:6]

vg_K = [0]
vg_K.extend(list(dfvg['K']))

vg_numU = [0]
vg_numU.extend(list(dfvg['num_U']))

vg_numO = [0]
vg_numO.extend(list(dfvg['num_O']))

vg_avg_kU = [0]
vg_avg_kU.extend(list(dfvg['avg_kU']))

vg_avg_kO = [0]
vg_avg_kO.extend(list(dfvg['avg_kO']))

plt.figure()
plt.plot(yr, vg_K,c='g')
plt.xlabel("Year")
plt.ylabel("K")
plt.savefig('plots/vg_ts_edges.png')

plt.figure()
plt.plot(yr, vg_numU,c='b')
plt.plot(yr, vg_numO,c='r')
plt.xlabel("Year")
plt.ylabel("Nodes")
plt.savefig('plots/vg_ts_nodes.png')

plt.figure()
plt.plot(yr, vg_avg_kU,c='b')
plt.plot(yr, vg_avg_kO,c='r')
plt.xlabel("Year")
plt.ylabel("Avg. degree")
plt.savefig('plots/vg_ts_avg.png')