import pandas as pd
import numpy as np
import datetime

# Enter in the CSVs you want to process:
df_EV = pd.read_csv('EV1.csv', header=None)
print("this is the first one")
print(df_EV)

# Will get rid of col labels later:
df_EV.columns =['Timestamp', 'Power']


# Make sure Timestamp type is datetime
df_EV['Timestamp'] = df_EV['Timestamp'].astype('datetime64')
print(len(df_EV['Timestamp']))

# Set DateTime column as index
df_EV.set_index('Timestamp', inplace=True)

# 300s stands for 5 min offset, add flag "closed='right' " to get it to do it down instead of up:
df_EV = df_EV.resample('3s').mean() # 300 seconds = 5 mins

print("this is the resampled one")
print(df_EV)

# Unindexing timestamp col:
#df_EV['Timestamp'] = df_EV.index


# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
df_EV.to_csv('EV1_Resampled.csv', header=False, index=True)
