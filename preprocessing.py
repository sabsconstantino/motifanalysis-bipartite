import pandas as pd

#-----------------------------------------------------------------------------
# music

df_music = pd.read_csv("data/ratings_music_videogames/ratings_Digital_Music.csv", header=None, names=['user','product','rating','timestamp'])

# complete dataset
# 478235 users, 266414 products
# 836006 rows
df_music['timestamp'] = pd.to_datetime(df_music['timestamp'],unit='s') 

# high rating
# 436127 users, 249582 products
# 744929 rows
df_music_HR = df_music[df_music['rating'] >= 4]

# 93157 users, 80851 products
# 142397 rows
df_music_HR_14 = df_music_HR[df_music_HR['timestamp'].dt.year == 2014]
df_music_HR_14 = df_music_HR_14[[0,1]]

# 157863 users, 135429 products
# 258755 rows
df_music_HR_13 = df_music_HR[df_music_HR['timestamp'].dt.year == 2013]
df_music_HR_13 = df_music_HR_13[[0,1]]

# 70641 users, 61469 products
# 101556 rows
df_music_HR_12 = df_music_HR[df_music_HR['timestamp'].dt.year == 2012]
df_music_HR_12 = df_music_HR_12[[0,1]]

# 23313 users, 17272 products
# 30764 rows
df_music_HR_11 = df_music_HR[df_music_HR['timestamp'].dt.year == 2011]
df_music_HR_11 = df_music_HR_11[[0,1]]

# 18642 users, 13001 products
# 23830 rows
df_music_HR_10 = df_music_HR[df_music_HR['timestamp'].dt.year == 2010]
df_music_HR_10 = df_music_HR_10[[0,1]]

# 19024 users, 11695 products
# 24676 rows
df_music_HR_09 = df_music_HR[df_music_HR['timestamp'].dt.year == 2009]
df_music_HR_09 = df_music_HR_09[[0,1]]

#-----------------------------------------------------------------------------
# video games

df_vg = pd.read_csv("data/ratings_music_videogames/ratings_Video_Games.csv", header=None, names=['user','product','rating','timestamp'])

# complete dataset
df_vg['timestamp'] = pd.to_datetime(df_vg['timestamp'],unit='s') 

# high rating
df_vg_HR = df_vg[df_vg['rating'] >= 4]

df_vg_HR_14 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2014]
df_vg_HR_14 = df_vg_HR_14[[0,1]]

df_vg_HR_13 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2013]
df_vg_HR_13 = df_vg_HR_13[[0,1]]

df_vg_HR_12 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2012]
df_vg_HR_12 = df_vg_HR_12[[0,1]]

df_vg_HR_11 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2011]
df_vg_HR_11 = df_vg_HR_11[[0,1]]

df_vg_HR_10 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2010]
df_vg_HR_10 = df_vg_HR_10[[0,1]]

df_vg_HR_09 = df_vg_HR[df_vg_HR['timestamp'].dt.year == 2009]
df_vg_HR_09 = df_vg_HR_09[[0,1]]
