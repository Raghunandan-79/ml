# head() tail() -> by default 5 rows
# head(n), tail(n)
import pandas as pd

df = pd.read_excel("/home/raghu/Documents/ml/libraries/pandas/basic/reading/SampleSuperstore.xlsx")

print("Displaying first 10 rows")
print(df.head(10))

print()

print("Displaying last 10 rows")
print(df.tail(10))