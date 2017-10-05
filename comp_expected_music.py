import numpy as np
import pandas as pd
import bip_degrees as bk
from collections import Counter

'''This module is for calculating the approximate expected numbers of each subgraph in the music dataset, using the equations proposed in Section 3.5 of the thesis. The percent differences are also calculated, as well as the maximum degrees and structural cutoff.
'''

M = np.array([len(bk.m00_kU.keys()), len(bk.m03_kU.keys()), len(bk.m06_kU.keys()), len(bk.m09_kU.keys()), len(bk.m12_kU.keys()), len(bk.m14_kU.keys())])
Mm1 = np.array([m-1 for m in M])
Mm2 = np.array([m-2 for m in M])

N = np.array([len(bk.m00_kO.keys()), len(bk.m03_kO.keys()), len(bk.m06_kO.keys()), len(bk.m09_kO.keys()), len(bk.m12_kO.keys()), len(bk.m14_kO.keys())])
Nm1 = np.array([n-1 for n in N])
Nm2 = np.array([n-2 for n in N])

K = np.array([sum(bk.m00_kU.values()), sum(bk.m03_kU.values()), sum(bk.m06_kU.values()), sum(bk.m09_kU.values()), sum(bk.m12_kU.values()), sum(bk.m14_kU.values())])

avg_kU = np.array([np.mean(bk.m00_kU.values()), np.mean(bk.m03_kU.values()), np.mean(bk.m06_kU.values()), np.mean(bk.m09_kU.values()), np.mean(bk.m12_kU.values()), np.mean(bk.m14_kU.values())])

avg_kUkm1 = np.array([np.mean([k*(k-1) for k in bk.m00_kU.values()]), np.mean([k*(k-1) for k in bk.m03_kU.values()]), np.mean([k*(k-1) for k in bk.m06_kU.values()]), np.mean([k*(k-1) for k in bk.m09_kU.values()]), np.mean([k*(k-1) for k in bk.m12_kU.values()]), np.mean([k*(k-1) for k in bk.m14_kU.values()])])

avg_kUkm1m2 = np.array([np.mean([k*(k-1)*(k-2) for k in bk.m00_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m03_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m06_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m09_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m12_kU.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m14_kU.values()])])

avg_kO = np.array([np.mean(bk.m00_kO.values()), np.mean(bk.m03_kO.values()), np.mean(bk.m06_kO.values()), np.mean(bk.m09_kO.values()), np.mean(bk.m12_kO.values()), np.mean(bk.m14_kO.values())])

avg_kOkm1 = np.array([ np.mean([k*(k-1) for k in bk.m00_kO.values()]), np.mean([k*(k-1) for k in bk.m03_kO.values()]), np.mean([k*(k-1) for k in bk.m06_kO.values()]), np.mean([k*(k-1) for k in bk.m09_kO.values()]), np.mean([k*(k-1) for k in bk.m12_kO.values()]), np.mean([k*(k-1) for k in bk.m14_kO.values()]) ])

avg_kOkm1m2 = np.array([np.mean([k*(k-1)*(k-2) for k in bk.m00_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m03_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m06_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m09_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m12_kO.values()]), np.mean([k*(k-1)*(k-2) for k in bk.m14_kO.values()])])

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

df00 = pd.read_csv('random_counts/samek_m9800.csv')
df03 = pd.read_csv('random_counts/samek_m9803.csv')
df06 = pd.read_csv('random_counts/samek_m9806.csv')
df09 = pd.read_csv('random_counts/samek_m9809.csv')
df12 = pd.read_csv('random_counts/samek_m9812.csv')
df14 = pd.read_csv('random_counts/samek_m9814.csv')

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
	[[Counter(bk.m00_kU).most_common(1)[0][1],Counter(bk.m03_kU).most_common(1)[0][1],Counter(bk.m06_kU).most_common(1)[0][1],Counter(bk.m09_kU).most_common(1)[0][1],Counter(bk.m12_kU).most_common(1)[0][1],Counter(bk.m14_kU).most_common(1)[0][1]],
	[Counter(bk.m00_kO).most_common(1)[0][1],Counter(bk.m03_kO).most_common(1)[0][1],Counter(bk.m06_kO).most_common(1)[0][1],Counter(bk.m09_kO).most_common(1)[0][1],Counter(bk.m12_kO).most_common(1)[0][1],Counter(bk.m14_kO).most_common(1)[0][1]],
	[k**0.5 for k in K]]
	)
M_cutoff = M_cutoff.transpose()

df_cutoff = pd.DataFrame(M_cutoff,columns=['max_kU','max_kO','sqrt(K)'])
df_cutoff['max_kU<sqrt(K)'] = df_cutoff['max_kU']<=df_cutoff['sqrt(K)']
df_cutoff['max_kO<sqrt(K)'] = df_cutoff['max_kO']<=df_cutoff['sqrt(K)']
print df_cutoff