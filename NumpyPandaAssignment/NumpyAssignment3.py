# Replace the values which are multiples of 5 by -1 using fancy indexing in [1,5,10,4,15,20,7,35]

import numpy as np

a = np.array([1, 5, 10, 4, 15, 20, 7, 35])

mask = (a % 5 == 0)

extract_from_a = a[mask]
print(extract_from_a)

a[mask] = -1

print(a)
