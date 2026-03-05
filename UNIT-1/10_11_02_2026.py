add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
operations = {"+": add, "-": sub, "*": mul, "/": div}

def demo():
    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Invalid operator!")

demo()
