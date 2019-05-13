'''
How to remove from one array those items that exist in another?
a = np.array([1, 2, 3, 4, 5]) b = np.array([5, 6, 3, 1, 4])
'''

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 3, 1, 4])

print(np.setdiff1d(a, b))