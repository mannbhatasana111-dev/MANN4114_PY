# Find Largest of Three Numbers

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
num3 = float(input("Enter Third Number : "))

print("The Largest Number Is:", largest_of_three(num1, num2, num3))
