'''
Import csv file using pd.read_csv method, Use the weather_data.csv from the pandas folder
'''

import pandas as pd
import os

# print(os.getcwd())
print(os.listdir(os.getcwd()))

# Datasource: https://geo-python.github.io/2017/_static/data/L5/Kumpula-June-2016-w-metadata.txt

df = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)

print(df)

'''
Obtain the columns, index and shape of the above data frame.
'''
print(df.columns)

print(df.index)

print(df.shape)

'''
Use describe method on the dataframe and write your conclusion
'''

# describe gives overview of the basic statistics for all attributes in our DataFrame
print(df.describe())