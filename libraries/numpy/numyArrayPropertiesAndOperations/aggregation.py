"""
summarizes the data like average

function      ->  what it does
np.sum(arr)   ->  add all
np.mean(arr)  ->  calculate average
np.min(arr)   ->  min value
np.max(arr)   ->  max value
np.std(arr)   ->  standard deviation
np.var(arr)   ->  variance
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))