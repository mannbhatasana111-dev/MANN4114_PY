import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

male_count = (df['Gender'] == 'Male').sum()
female_count = (df['Gender'] == 'Female').sum()

labels = ['Male', 'Female']
counts = [male_count, female_count]

plt.bar(labels, counts, color=['blue', 'pink'])

plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.title("Male vs Female Students")

plt.show()