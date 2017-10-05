import numpy as np
import pandas as pd
import bip_degrees as bk
from collections import Counter

'''This module is for calculating the approximate expected numbers of each subgraph in the music dataset, using the equations proposed in Section 3.5 of the thesis. The percent differences are also calculated, as well as the maximum degrees and structural cutoff.
'''

M = np.array([len(bk.vg00_kU.keys()), len(bk.vg03_kU.keys()), len(bk.vg06_kU.keys()), len(bk.vg09_kU.keys()), len(bk.vg12_kU.keys()), len(bk.vg14x_kU.keys())])
Mm1 = np.array([m-1 for m in M])
Mm2 = np.array([m-2 for m in M])

N = np.array([len(bk.vg00_kO.keys()), len(bk.vg03_kO.keys()), len(bk.vg06_kO.keys()), len(bk.vg09_kO.keys()), len(bk.vg12_kO.keys()), len(bk.vg14x_kO.keys())])
Nm1 = np.array([n-1 for n in N])
Nm2 = np.array([n-2 for n in N])

K = np.array([sum(bk.vg00_kU.values()), sum(bk.vg03_kU.values()), sum(bk.vg06_kU.values()), sum(bk.vg09_kU.values()), sum(bk.vg12_kU.values()), sum(bk.vg14x_kU.values())])

avg_kU = np.array([np.mean(bk.vg00_kU.values()), np.mean(bk.vg03_kU.values()), np.mean(bk.vg06_kU.values()), np.mean(bk.vg09_kU.values()), np.mean(bk.vg12_kU.values()), np.mean(bk.vg14x_kU.values())])

avg_kUkm1 = np.array([np.mean([k*(k-1) for k in bk.vg00_kU.values()]), np.mean([k*(k-1) for k in bk.vg03_kU.values()]), np.mean([k*(k-1) for k in bk.vg06_kU.values()]), np.mean([k*(k-1) for k in bk.vg09_kU.values()]), np.mean([k*(k-1) for k in bk.vg12_kU.values()]), np.mean([k*(k-1) for k in bk.vg14x_kU.values()])])

avg_kUkm1m2 = np.array([np.mean([k*(k-1)*(k-2) for k in bk.vg00_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg03_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg06_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg09_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg12_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg14x_kU.values()])])

avg_kO = np.array([np.mean(bk.vg00_kO.values()), np.mean(bk.vg03_kO.values()), np.mean(bk.vg06_kO.values()), np.mean(bk.vg09_kO.values()), np.mean(bk.vg12_kO.values()), np.mean(bk.vg14x_kO.values())])

avg_kOkm1 = np.array([ np.mean([k*(k-1) for k in bk.vg00_kO.values()]), np.mean([k*(k-1) for k in bk.vg03_kO.values()]), np.mean([k*(k-1) for k in bk.vg06_kO.values()]), np.mean([k*(k-1) for k in bk.vg09_kO.values()]), np.mean([k*(k-1) for k in bk.vg12_kO.values()]), np.mean([k*(k-1) for k in bk.vg14x_kO.values()]) ])

avg_kOkm1m2 = np.array([np.mean([k*(k-1)*(k-2) for k in bk.vg00_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg03_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg06_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg09_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg12_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.vg14x_kO.values()])])

# -------------------------------------------------------

exp_S = np.zeros((8,6))

exp_S[0] = avg_kUkm1 / 2 * M
exp_S[1] = avg_kOkm1 / 2 * N

exp_S[4] = (avg_kOkm1*avg_kOkm1 * avg_kUkm1*avg_kUkm1) / (2*avg_kU * avg_kU * avg_kO * avg_kO)
exp_S[2] = (avg_kUkm1)*M*Mm1/4 - exp_S[4]
exp_S[3] = avg_kOkm1 * avg_kUkm1 / (2*K) * Mm1 * Nm1

exp_S[5] = (avg_kUkm1 * avg_kUkm1 * avg_kOkm1m2 * avg_kOkm1) / (2 * avg_kU * avg_kU * avg_kO * avg_kO)
exp_S[6] = (avg_kOkm1*avg_kOkm1 * avg_kUkm1m2 * avg_kUkm1) / (2 * avg_kU * avg_kU * avg_kO * avg_kO)
exp_S[7] = (2* avg_kUkm1*avg_kUkm1*avg_kUkm1*avg_kOkm1m2*avg_kOkm1m2) / K / (avg_kU*avg_kU*avg_kU*avg_kO*avg_kO)

exp_S = exp_S.transpose()

# -------------------------------------------------------

df00 = pd.read_csv('random_counts/samek_vg9700.csv')
df03 = pd.read_csv('random_counts/samek_vg9703.csv')
df06 = pd.read_csv('random_counts/samek_vg9706.csv')
df09 = pd.read_csv('random_counts/samek_vg9709.csv')
df12 = pd.read_csv('random_counts/samek_vg9712.csv')
df14 = pd.read_csv('random_counts/samek_vg9714x.csv')

act_S = np.zeros((6,8))

act_S[0] = np.mean(df00.as_matrix(),axis=0)
act_S[1] = np.mean(df03.as_matrix(),axis=0)
act_S[2] = np.mean(df06.as_matrix(),axis=0)
act_S[3] = np.mean(df09.as_matrix(),axis=0)
act_S[4] = np.mean(df12.as_matrix(),axis=0)
act_S[5] = np.mean(df14.as_matrix(),axis=0)

pct_diff = (act_S - exp_S)/act_S * 100
#pct_diff = (act_S-exp_S)/exp_S*100
print pct_diff

# -------------------------------------------------------

M_cutoff = np.array(
	[[Counter(bk.vg00_kU).most_common(1)[0][1],Counter(bk.vg03_kU).most_common(1)[0][1],Counter(bk.vg06_kU).most_common(1)[0][1],Counter(bk.vg09_kU).most_common(1)[0][1],Counter(bk.vg12_kU).most_common(1)[0][1],Counter(bk.vg14x_kU).most_common(1)[0][1]],
	[Counter(bk.vg00_kO).most_common(1)[0][1],Counter(bk.vg03_kO).most_common(1)[0][1],Counter(bk.vg06_kO).most_common(1)[0][1],Counter(bk.vg09_kO).most_common(1)[0][1],Counter(bk.vg12_kO).most_common(1)[0][1],Counter(bk.vg14x_kO).most_common(1)[0][1]],
	[k**0.5 for k in K]]
	)
M_cutoff = M_cutoff.transpose()

df_cutoff = pd.DataFrame(M_cutoff,columns=['max_kU','max_kO','sqrt(K)'])
df_cutoff['max_kU<sqrt(K)'] = df_cutoff['max_kU']<=df_cutoff['sqrt(K)']
df_cutoff['max_kO<sqrt(K)'] = df_cutoff['max_kO']<=df_cutoff['sqrt(K)']
print df_cutoff