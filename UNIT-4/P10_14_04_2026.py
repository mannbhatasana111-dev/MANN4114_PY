import re

file = open("student.txt", "r")

pattern = r"\b\d{2}-\d{10}\b"

for line in file:
    if re.search(pattern, line):
        print(line.strip())

file.close()