'''
How to combine two series into a dict
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz')) ser2 = pd.Series(np.arange(26))
'''

import pandas as pd
import numpy as np

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# print(np.arange(26))
# using zip() to convert lists to dictionary
res = dict(zip(ser1, ser2))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))
