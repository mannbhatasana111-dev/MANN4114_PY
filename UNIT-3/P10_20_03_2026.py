class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

n1 = Number(a)
n2 = Number(b)

print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)