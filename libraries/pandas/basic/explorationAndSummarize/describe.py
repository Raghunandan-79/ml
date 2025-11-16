"""
    provides a summary of descriptive statistics for numerical 
    columns in your data frame
"""
import pandas as pd

# step 1 -> sample data frame

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, 34, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score":[85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

print("Sample Data Frame")
print(df)
print()
print("Descriptive statistics")
print(df.describe())