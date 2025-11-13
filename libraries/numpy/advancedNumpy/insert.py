"""
    np.insert(array, index, value, asix=None)
    array -> original array
    index -> position
    value -> data
    axis -> None -> 1d array, 0 -> row-wise, 1 -> column wise
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
new_arr = np.insert(arr, 2, 100, axis=None)
print(new_arr)