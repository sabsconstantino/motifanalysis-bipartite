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

df_vg_00 = df_vg[df_vg['timestamp'].dt.year <= 2000]
df_vg_00 = df_vg_00[[0,1]]

df_vg_03 = df_vg[df_vg['timestamp'].dt.year <= 2003]
df_vg_03 = df_vg_03[[0,1]]

df_vg_06 = df_vg[df_vg['timestamp'].dt.year <= 2006]
df_vg_06 = df_vg_06[[0,1]]

df_vg_09 = df_vg[df_vg['timestamp'].dt.year <= 2009]
df_vg_09 = df_vg_09[[0,1]]

df_vg_12 = df_vg[df_vg['timestamp'].dt.year <= 2012]
df_vg_12 = df_vg_12[[0,1]]

# video games 1997-2014 with most purchased object
df_vg_14 = df_vg[df_vg['timestamp'].dt.year <= 2014]
df_vg_14 = df_vg_14[[0,1]]

# video games 1997-2014 WITHOUT most-bought object
most_purchased = df_vg_14['product'].value_counts().idxmax()
df_vg_14x = df_vg_14[ df_vg_14['product'] != most_purchased]