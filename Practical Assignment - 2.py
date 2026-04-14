print('-----Arithmetic Operation------')

#1 Arithmetic Operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    print("Result:", add(num1, num2))
elif choice == "-":
    print("Result:", subtract(num1, num2))
elif choice == "*":
    print("Result:", multiply(num1, num2))
elif choice == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")

print()


print('-----Largest Of Three Numbers------')

#2 Largest of Three Numbers

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number:", largest(x, y, z))

print()


print('-----Factorial Program------')

#3 Factorial Program

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)


num = int(input("Enter number: "))

print("Factorial (Normal):", factorial(num))
print("Factorial (Recursive):", factorial_recursive(num))

print()


print('-----Simple Interest------')

#4 Simple Interest

def simple_interest(p, t, r=5):
    return (p * t * r) / 100


principal = float(input("Enter principal amount: "))
time = float(input("Enter time: "))

print("Simple Interest:", simple_interest(principal, time))

print()


print('-----Function Inside Function------')

#5 Function Inside Another Function

def outer():
    print("Outer function executed")

    def inner():
        print("Inner function executed")

    inner()


outer()

print()


print('-----Banking System------')

#6 Simple Banking System

balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    return balance

def check_balance():
    return balance


amount = float(input("Enter deposit amount: "))
print("Balance after deposit:", deposit(amount))

amount = float(input("Enter withdraw amount: "))
print("Balance after withdraw:", withdraw(amount))

print("Current Balance:", check_balance())

print()


print('-----Student Result System------')

#7 Student Result System

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

marks = []

for i in range(5):
    m = float(input("Enter marks for subject " + str(i+1) + ": "))
    marks.append(m)

percentage = calculate_percentage(marks)

print("Percentage:", percentage)
print("Grade:", assign_grade(percentage))
