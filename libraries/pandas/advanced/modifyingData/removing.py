import pandas as pd

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, 34, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score":[85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# drop method
# df.drop(columns = ["ColumnName"], inplace=True)

# removing single column
df.drop(columns=["Performance_Score"], inplace=True)
print(df)

print()

df.drop(columns=["Age", "Name"], inplace=True)
print(df)