'''
Reshape an array np.array([1, 2, 3, 4], ndmin=2) using ravel
and identify the shape, dimensions and write your conclusions
'''

import numpy as np

a = np.array([1, 2, 3, 4], ndmin=2)

print(np.ravel(a))

print("Shape of Array A:", a.shape)

print("Dimension of Array A :", a.ndim)

'''
Here we see that after applying ravel, the array is flattened as 1D and it still has 2 dimensions
and the shape shows that row has 1 element and column has 4 elements
'''