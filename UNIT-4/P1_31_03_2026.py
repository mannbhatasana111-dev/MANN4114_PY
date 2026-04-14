import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('student.csv')

print("--- Columns in the File ---")
print(df.columns.tolist())

print("--- Data Type of Each Column ---")
print(df.dtypes)

print("--- Data Preview (First 5 Records) ---")
print(df.head())