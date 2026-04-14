import matplotlib.pyplot as plt

courses = []
students = []

n = int(input("Enter number of courses: "))

for i in range(n):
    name = input("Enter course name: ")
    count = int(input("Enter number of students: "))

    courses.append(name)
    students.append(count)

max_index = students.index(max(students))

explode = [0] * n
explode[max_index] = 0.2

plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')

plt.title("Course-wise Student Distribution")

plt.show()