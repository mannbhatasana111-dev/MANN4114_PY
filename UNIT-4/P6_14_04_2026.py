import matplotlib.pyplot as plt

ages = []

for i in range(10):
    age = int(input("Enter age: "))
    ages.append(age)

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, color='skyblue', edgecolor='black')

plt.xlabel("Age Groups")
plt.ylabel("Number of Students")
plt.title("Histogram of Student Ages")

plt.show()