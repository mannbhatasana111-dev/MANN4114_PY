class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print("--- Student Details ---")
        print(f"Roll No : {self.rollno}")
        print(f"Name    : {self.name}")
        print(f"Gender  : {self.gender}")
        print(f"Age     : {self.age}")


class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        super().display_student()
        print("\n--- Course Details ---")
        print(f"Course  : {self.coursename}")
        print(f"Duration: {self.duration}")
        print(f"Fee     : ₹{self.fee}")


print("Enter Student Details:")
user_rollno = int(input("Roll No: "))
user_name = input("Name: ")
user_gender = input("Gender: ")
user_age = int(input("Age: "))

print("\nEnter Course Details:")
user_course = input("Course Name: ")
user_duration = input("Duration (e.g., 3 Years): ")
user_fee = int(input("Fee Amount: "))

my_enrollment = Course(user_rollno, user_name, user_gender, user_age, user_course, user_duration, user_fee)

print("\n")
my_enrollment.display_course()