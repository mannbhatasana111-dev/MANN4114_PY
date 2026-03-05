# Input marks And Calculate Percentage Grade etc
m1 = int(input('Enter the PYTHON MARK : '))
m2 = int(input('Enter the ANDROID MARK : '))
m3 = int(input('Enter the NETWORKING MARK : '))
m4 = int(input('Enter the OS MARK : '))

total = m1 + m2 + m3 + m4
percent = total / 4

if percent >= 90:
    grade = "O"
elif 80 <= percent < 90:
    grade = "A"
elif 70 <= percent < 80:
    grade = "B"
elif 60 <= percent < 70:
    grade = "C"
elif 50 <= percent < 60:
    grade = "D"
elif 40 <= percent < 50:
    grade = "E"
else:
    grade = "FAIL"

print("\n----- RESULT -----")
print(f"PYTHON     | {m1}")
print(f"ANDROID    | {m2}")
print(f"NETWORKING | {m3}")
print(f"OS         | {m4}")
print(f"TOTAL      | {total}")
print(f"PERCENTAGE | {percent:.2f}")
print(f"GRADE      | {grade}")
