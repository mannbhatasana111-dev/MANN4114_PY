class Student:
    
    def AddStudent(self):
        print("--- Please Enter Student Details ---")
        self.roll_no = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")
        print("Student added successfully!\n")
        
    def Display(self):
        print("--- Student Information ---")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Gender  : {self.gender}")
        print("---------------------------\n")

student1 = Student()

student1.AddStudent()      
student1.Display()  
