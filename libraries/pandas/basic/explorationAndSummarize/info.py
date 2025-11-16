import pandas as pd

df = pd.read_excel("/home/raghu/Documents/ml/libraries/pandas/basic/reading/SampleSuperstore.xlsx")

print("Displaying the info of data set")
print(df.info())