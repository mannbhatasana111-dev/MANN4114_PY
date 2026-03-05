try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")

except ValueError:
    print("Error: You must enter whole numbers!")

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except Exception as e:
    print(f"Something else went wrong: {e}")