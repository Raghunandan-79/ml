import pandas as pd

# read data from CSV file into a dataframe
# df = pd.read_csv("/home/raghu/Documents/ml/libraries/pandas/basic/reading/cab_rides.csv", encoding="utf-8")

# read excel
# df = pd.read_excel("/home/raghu/Documents/ml/libraries/pandas/basic/reading/SampleSuperstore.xlsx")

df = pd.read_json("/home/raghu/Documents/ml/libraries/pandas/basic/reading/sample_Data.json")

print(df)