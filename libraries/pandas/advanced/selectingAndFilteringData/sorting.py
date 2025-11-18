# Sorting data

# sorting data in 1 column -> sort_values()
# df.sort_values(by="Column_Name", True, inplace=True) -> ascending or False -> descending
import pandas as pd

data = {
    "Name":["Arun", "Varun", "Karun"],
    "Age":[28, 34, 22],
    "Salary":[10000, 20000, 30000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)

print("Sorted age by Descending")
print(df)