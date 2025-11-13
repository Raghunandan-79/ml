"""
    reshape(rows, columns) specify new shape
    if dimensions match.
    It does not creates a copy, it returns view 
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = arr.reshape(2, 3)
print(reshaped_array)