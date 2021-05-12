# Data Resampler
### A resolution decreasing program.


## Project Description
This program iterates through EV profiles with a 10-minute sampling rate and converts it to 15 minutes, outputting the new profiles in resampled_data. The output rate doesn't necessarily have to be 15 minutes and can be varied, as long as it remains at a resolution that is lower than that of the input CSVs. The program averages the values in between and ceils any values larger than a 0 and less than 5.76 kW to 5.76 kW. Due to this, this script specific for EV profiles with a power rating of 5.76 kW and it would need to be accordingly adjusted for profiles with different power ratings.

## Requirements
This program only works on Windows due to the directory convention used. 
You need to have the load profiles as CSVs in their respective directory inside the data directory. **NOTE:** make sure to remove placeholder.txt
```
pip install pandas numpy
```

### To get the code
```
git clone https://github.com/neighdeen84/Data_Resampler.git
```


## Usage
```
cd Data_Resampler
python main.py
```


