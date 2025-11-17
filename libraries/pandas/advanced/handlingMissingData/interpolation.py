"""
    Techique which we can use to fill estimated value instead of missing value
    It helps in maintaining consistency in data

    Why use ?
        1. Preserve data integrity
        2. Smooth trends
        3. Avoid data loss

    interpolate()

    When to use ?

        1. Time Series Data
        2. Numeric Data with Trends
        3. Avoid Dropping Rows
"""
import pandas as pd

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, None, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score":[85, None, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# linear, polynomial, time

# linear
print("Before interpolation")
print(df)

print()

print("After Interpolation")
df["Age"] = df["Age"].interpolate(method="linear")
print(df)