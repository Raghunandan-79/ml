"""
    Common Aggregation Functions
    1 -> sum()
    2 -> mean()
    3 -> count()
    4 -> min()
    5 -> max()
    6 -> std()
"""

import pandas as pd

data = {
    "Name":["Arun", "Varun", "Karun", "Narun", "Marun"],
    "Age":[28, 34, 22, 34, 28],
    "Salary":[50000, 60000, 45000, 52000, 48000]
}

df = pd.DataFrame(data)

grouped = df.groupby(["Age", "Name"])["Salary"].sum()

print(grouped)