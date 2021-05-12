### NOTE: This is for EV profiles specifically, because of the ceiling that gets implemented.
import pandas as pd
import numpy as np
import shutil
import os

def iter_files(folder_path):
    resampled_dir = os.getcwd()+ '\\resampled_data'
    print(resampled_dir)
    os.chdir(folder_path)

    if os.path.isdir(resampled_dir):
        shutil.rmtree(resampled_dir)
        os.mkdir(resampled_dir)
    else:
        os.mkdir(resampled_dir)
    for filename in os.listdir(folder_path):
        # Enter in the CSVs you want to process:
        # Note: if the CSV has no header use: header = None
        # if it has a header use: header = 0
        print(filename)
        df_EV = pd.read_csv(filename, header=None)
        df_2 =  pd.read_csv(filename, header=None)


        #### using the good timestamp:
        # Give labels & make sure Timestamp type is datetime
        df_2.columns =['Timestamp', 'Power']

        df_2['Timestamp'] = df_2['Timestamp'].astype('datetime64')

        # Set DateTime column as index
        df_2.set_index('Timestamp', inplace=True)

        # 900s stands for 15 min offset, add flag "closed='right' " to get it to do it down instead of up:
        df_2 = df_2.resample('900s').mean()

        # Getting rid of the aliased power column:
        del df_2['Power']

        # Unindexing timestamp col:
        df_2.reset_index(level=0, inplace=True)


        #### Averaging:
        # Will get rid of col labels later:
        df_EV.columns =['Date', 'Power']
        del df_EV['Date']


        step = 900 # 15 mins
        df_EV = df_EV.groupby(df_EV.index // step).mean()

        dfT = pd.concat([df_2, df_EV], axis=1)

        # Reduce to one decimal place:
        dfT.Power = df_EV.Power.round(2)

        # Getting rid of the last NaN value:
        dfT.dropna(inplace= True)
        #print(dfT)

        # Ceil values less than 5760:
        dfT['Power'] = np.where( (dfT.Power > 0) & (dfT.Power < 5760) , 5760, dfT.Power)
        # Printing out sampled CSV with removed headers (col labels) and keeping the index (timestamp col):
        dfT.to_csv(resampled_dir+'\\'+filename, header=False, index=False)


cwd = os.getcwd()
data_dir = cwd + '\\data'

iter_files(data_dir)