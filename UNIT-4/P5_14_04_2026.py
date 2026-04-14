import matplotlib.pyplot as plt

companies = []
employees = []

for i in range(5):
    name = input("Enter company name: ")
    size = int(input("Enter number of employees: "))

    companies.append(name)
    employees.append(size)

colors = ['red', 'blue', 'green', 'orange', 'purple']

plt.bar(companies, employees, color=colors)

plt.xlabel("Companies")
plt.ylabel("Employee Size")
plt.title("Company Employee Data")

plt.show()