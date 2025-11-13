"""
    np.nan_to_num(array, nan=value) default=0
    changes nan value to some number
"""

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

cleaned_arr = np.nan_to_num(arr, nan=100)
print(cleaned_arr)