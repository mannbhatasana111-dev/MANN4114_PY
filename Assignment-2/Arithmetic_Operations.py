# Arithmetic operation functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == '1':
    print(f"Result : {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result : {num1} - {num2} = {subtract(num1,num2)}")
elif choice == '3':
    print(f"Result : {num1} * {num2} = {multiply(num1,num2)}")
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")

