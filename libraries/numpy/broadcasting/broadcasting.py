""""
    It expands smaller arrays into larger arrays
    three rules of broadcasting
    1. matching dimensions
    2. expanding single elements
    3. incompatible shapes --> throws error
"""

import numpy as np

prices = np.array([100, 200, 300])
discount = 10

final_prices = prices - (prices * discount / 100)

print(final_prices)