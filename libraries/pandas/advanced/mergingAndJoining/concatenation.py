"""
    Combining data frame either vertically or horizontally

    pd.concate([df1, df2], axis=0, ignore_index=True)

    [df1, df2]
    axis = 0 row-wise or 1 for column-wise

    ignore_index = True -> index reset
"""

import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerID":[1, 2],
    "Name":["Gopal", "Raju"]
})

df_region2 = pd.DataFrame({
    "CustomerID":[3, 4],
    "Name":["Shyam", "Baburao"]
})

# concatenate vertically
df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)

print(df_concat)