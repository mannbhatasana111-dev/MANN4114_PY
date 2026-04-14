import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv('student.csv')

rajkot_students = df[df['City'] == 'Rajkot']
male_students = df[df['Gender'] == 'Male']
male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]
age_20_plus = df[df['Age'] >= 20]

print("--- Students from Rajkot City ---")
print(rajkot_students)

print("\n" + "="*50 + "\n")

print("--- Male Students ---")
print(male_students)

print("\n" + "="*50 + "\n")

print("--- Male Students from Rajkot City ---")
print(male_rajkot)

print("\n" + "="*50 + "\n")

print("--- Students whose Age >= 20 ---")
print(age_20_plus)