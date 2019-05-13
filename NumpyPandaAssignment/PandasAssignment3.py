'''
How to convert a numpy array to a dataframe of given shape?
a = pd.Series(np.random.randint(1, 10, 35))
'''

import pandas as pd
import numpy as np

# numpy.random.randint() returns an array with random integers from low(1) to high(10) with size as 35
a = pd.Series(np.random.randint(1, 10, 35))

df = pd.DataFrame(a.values.reshape(7, 5))

print(df)
