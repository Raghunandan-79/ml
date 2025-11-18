# pd.merge(DataFrame1, DataFrame2, on="Column_Name", how="Type of join")

import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    "CustomerID":[1, 2, 3],
    "Name":["Ramesh", "Suresh", "Kalpesh"]
})

# order dataframe
df_orders = pd.DataFrame({
    "CustomerID":[1, 2, 4],
    "OrderAmount":[250, 450, 350]
})

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print("Right join")
print(df_merged)

"""
1df = m rows
2df = n rown
m * n rows
"""