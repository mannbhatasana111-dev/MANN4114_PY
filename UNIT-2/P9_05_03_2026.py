import os

FILE_NAME = "students_data.txt"


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{grade}\n")
    print("Student added successfully!")


def list_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    print(f"\n{'Roll':<10} {'Name':<20} {'Grade'}")
    print("-" * 40)
    with open(FILE_NAME, "r") as f:
        for line in f:
            r, n, g = line.strip().split(',')
            print(f"{r:<10} {n:<20} {g}")


def search_student():
    roll_to_find = input("Enter Roll No to search: ")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            r, n, g = line.strip().split(',')
            if r == roll_to_find:
                print(f"Found! Name: {n}, Grade: {g}")
                found = True
                break
    if not found:
        print("Student not found.")


def delete_student():
    roll_to_del = input("Enter Roll No to delete: ")
    lines = []
    found = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if line.split(',')[0] != roll_to_del:
                    f.write(line)
                else:
                    found = True
        print("Deleted successfully!") if found else print("Not found.")


def update_student():
    roll_to_upd = input("Enter Roll No to update: ")
    lines = []
    found = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if line.split(',')[0] == roll_to_upd:
                    name = input("Enter new Name: ")
                    grade = input("Enter new Grade: ")
                    f.write(f"{roll_to_upd},{name},{grade}\n")
                    found = True
                else:
                    f.write(line)
        print("Updated successfully!") if found else print("Not found.")


# Main Menu
while True:
    print("\n--- Student Management ---")
    print("a) Add Student\nb) Search Student\nc) List All\nd) Update\ne) Delete\nf) Exit")
    choice = input("Choice: ").lower()

    if choice == 'a':
        add_student()
    elif choice == 'b':
        search_student()
    elif choice == 'c':
        list_students()
    elif choice == 'd':
        update_student()
    elif choice == 'e':
        delete_student()
    elif choice == 'f':
        break
    else:
        print("Invalid choice!")