'''
How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
a = pd.Series(np.random.normal(10, 5, 25))
'''

import pandas as pd
import numpy as np

a = pd.Series(np.random.normal(10, 5, 25))


# print(a)
print("Minimum :", np.min(a))
print("Max :", np.max(a))

print("25th percentile :", np.percentile(a, 25))

print("Median :", np.percentile(a, 50))

print("75th percentile :", np.percentile(a, 75))

