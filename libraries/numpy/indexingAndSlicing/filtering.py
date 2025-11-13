""" 
    Boolean Masking: Filters the data according to 
    the condition given by the user
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[arr > 25])