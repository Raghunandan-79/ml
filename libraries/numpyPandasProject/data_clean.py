import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("/home/raghu/Documents/ml/libraries/numpyPandasProject/indian_employee_data_1000.csv")

# Convert "inf" and "-inf" strings to actual numeric infinity
df["Experience (Years)"] = pd.to_numeric(df["Experience (Years)"], errors="coerce")
df["Salary (INR)"] = pd.to_numeric(df["Salary (INR)"], errors="coerce")
df["Performance Rating"] = pd.to_numeric(df["Performance Rating"], errors="coerce")

# Missing values check
print("Missing values:")
print(df.isnull().sum())

# Fill numeric missing values
df["Salary (INR)"].fillna(df["Salary (INR)"].mean(), inplace=True)
df["Experience (Years)"].fillna(df["Experience (Years)"].mean(), inplace=True)
df["Performance Rating"].fillna(df["Performance Rating"].median(), inplace=True)

# Replace inf and -inf
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill remaining numeric NaN values
numeric_cols = df.select_dtypes(include=['float64','int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace negative salaries
df["Salary (INR)"] = df["Salary (INR)"].apply(lambda x: df["Salary (INR)"].mean() if x < 0 else x)

# Outlier removal using 3 SD rule
salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[(df["Salary (INR)"] >= lower_bound) & (df["Salary (INR)"] <= upper_bound)]

# Save cleaned CSV
df.to_csv("Cleaned-Indian-Employee-Data.csv", index=False)

print("Data Cleaning Completed. File Saved!")