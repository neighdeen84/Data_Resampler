import pandas as pd
import numpy as np
import datetime

# Enter in the CSVs you want to process:
df_EV = pd.read_csv('dryer_profile_611_1.csv', header=None)
df_2 = pd.read_csv('dryer_profile_611_1.csv', header=None)


#### using the good timestamp:
# Give labels & make sure Timestamp type is datetime
df_2.columns =['Timestamp', 'Power']
df_2['Timestamp'] = df_2['Timestamp'].astype('datetime64')

# Set DateTime column as index
df_2.set_index('Timestamp', inplace=True)

# 300s stands for 5 min offset, add flag "closed='right' " to get it to do it down instead of up:
df_2 = df_2.resample('300s', label='right',closed='right').mean()

# Getting rid of the aliased power column:
del df_2['Power']

# Unindexing timestamp col:
df_2.reset_index(level=0, inplace=True)



#### Averaging:
# Will get rid of col labels later:
df_EV.columns =['Date', 'Power']
del df_EV['Date']
#print('this is the length before:')
#print(len(df_EV))

step = 300 # 5 mins
df_EV = df_EV.groupby(df_EV.index // step).mean()
#print('this is the length after:')
#print(len(df_EV))

dfT = pd.concat([df_2, df_EV], axis=1)
dfT.replace(np.nan, 0, inplace=True)
print(dfT)


# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
dfT.to_csv('Resampled.csv', header=False, index=False)
