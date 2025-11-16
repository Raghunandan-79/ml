import pandas as pd

data = {
    "Name":['Ram', "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdeesh", "Raj", "Simran"],
    "Age":[28, 34, 22, 30, 29, 48, 25, 32],
    "Salary":[50000, 40000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score":[85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

# single conditions

high_salary = df[df['Salary'] > 50000]
print("Employee with salry greater than 50000")
print(high_salary)

print()
# multiple conditions
filtered = df[(df['Salary'] > 30000) & (df['Salary'] < 50000)]
print("Employee with salary greater than 20000 and less than 50000")
print(filtered)