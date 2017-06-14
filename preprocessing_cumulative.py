import pandas as pd

#-----------------------------------------------------------------------------
# music

df_m = pd.read_csv("data/ratings_music_videogames/ratings_Digital_Music.csv", header=None, names=['user','product','rating','timestamp'])

# complete dataset
df_m['timestamp'] = pd.to_datetime(df_m['timestamp'],unit='s') 

# drop ratings below 4
df_m = df_m[df_m['rating'] >= 4]

df_m_00 = df_m[df_m['timestamp'].dt.year <= 2000]
df_m_00 = df_m_00[[0,1]]

df_m_03 = df_m[df_m['timestamp'].dt.year <= 2003]
df_m_03 = df_m_03[[0,1]]

df_m_06 = df_m[df_m['timestamp'].dt.year <= 2006]
df_m_06 = df_m_06[[0,1]]

df_m_09 = df_m[df_m['timestamp'].dt.year <= 2009]
df_m_09 = df_m_09[[0,1]]

df_m_12 = df_m[df_m['timestamp'].dt.year <= 2012]
df_m_12 = df_m_12[[0,1]]

df_m_14 = df_m[df_m['timestamp'].dt.year <= 2014]
df_m_14 = df_m_14[[0,1]]

#-----------------------------------------------------------------------------
# video games

df_vg = pd.read_csv("data/ratings_music_videogames/ratings_Video_Games.csv", header=None, names=['user','product','rating','timestamp'])

# drop ratings below 4
df_vg = df_vg[df_vg['rating'] >= 4]

# complete dataset
df_vg['timestamp'] = pd.to_datetime(df_vg['timestamp'],unit='s') 

df_vg_02 = df_vg[df_vg['timestamp'].dt.year <= 2002]
df_vg_02 = df_vg_02[[0,1]]

df_vg_05 = df_vg[df_vg['timestamp'].dt.year <= 2005]
df_vg_05 = df_vg_05[[0,1]]

df_vg_08 = df_vg[df_vg['timestamp'].dt.year <= 2008]
df_vg_08 = df_vg_08[[0,1]]

df_vg_11 = df_vg[df_vg['timestamp'].dt.year <= 2011]
df_vg_11 = df_vg_11[[0,1]]

df_vg_14 = df_vg[df_vg['timestamp'].dt.year <= 2014]
df_vg_14 = df_vg_14[[0,1]]