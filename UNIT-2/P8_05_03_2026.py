try:
    print(f"{'Roll':<6} {'Name':<10} {'Total':<8} {'Per%':<8} {'Grade'}")
    print("-" * 45)

    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split(',')

            roll_no = data[0]
            name = data[1]
            marks = [int(m) for m in data[2:]]

            total = sum(marks)
            percentage = total / 4

            if percentage >= 80:
                grade = "A+"
            elif percentage >= 60:
                grade = "A"
            elif percentage >= 40:
                grade = "B"
            else:
                grade = "Fail"

            print(f"{roll_no:<6} {name:<10} {total:<8} {percentage:<8.2f} {grade}")

except FileNotFoundError:
    print("Error: The file 'students.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")