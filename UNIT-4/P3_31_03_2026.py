import pandas as pd
import numpy as np

df = pd.read_csv('student.csv')
df.loc[0, 'City'] = np.nan  # Creating a null value for demo

df_dropped = df.dropna()
df_filled = df.fillna("Unknown")

print("Rows after dropna:", len(df_dropped))
print("Rows after fillna:", len(df_filled))
