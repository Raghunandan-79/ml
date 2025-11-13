"""
    dividing array

    np.split() --> equal parts
    np.hsplit() --> horizontal split
    np.vsplit() --> vertically split
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

print(np.split(arr, 2))