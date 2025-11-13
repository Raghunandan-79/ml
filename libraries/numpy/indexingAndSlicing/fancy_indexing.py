# selecting multiple indexes at one time, creates copy
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[[0, 2, 4]]) # 1, 3, 5