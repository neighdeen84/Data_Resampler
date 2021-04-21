import pandas as pd
import numpy as np
import datetime

# Enter in the CSVs you want to process:
# Note: if the CSV has no header use: header = None
# if it has a header use: header = 0
df_EV = pd.read_csv('EV1.csv', header=0)
df_2 = pd.read_csv('EV1.csv', header=0)

print(df_2)
#### using the good timestamp:
# Give labels & make sure Timestamp type is datetime
df_2.columns =['Timestamp', 'Power']
print(df_2)

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
#dfT.replace(np.nan, 0, inplace=True)

# Reduce to one decimal place:
dfT.Power = df_EV.Power.round(2)

# Getting rid of the last NaN value:
dfT.dropna(inplace= True)
print(dfT)


# Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
dfT.to_csv('EV1_Resampled.csv', header=False, index=False)
