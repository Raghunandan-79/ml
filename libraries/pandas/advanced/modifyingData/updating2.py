import pandas as pd

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, 34, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score":[85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# increasing salary by 5%
df["Salary"] = df["Salary"] * 1.05
print(df)