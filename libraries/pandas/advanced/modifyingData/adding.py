import pandas as pd

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, 34, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score":[85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# adding columns
# square brackets df["Column_Name"] = some data

print(df)
print()

df["Bonus"] = df["Salary"] * 0.1
print(df)# adding columns
print()# adding columns# adding columns# adding columns# adding columns

# using insert()
# df.insert(location, "Column_Name", Some data)
df.insert(0, "Employee Id", [10, 20, 30, 40, 50, 60, 70, 80])
print(df)