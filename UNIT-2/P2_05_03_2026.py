class MyError(Exception):
    pass

try:
    age = int(input("Enter the Age: "))

    if age < 18:
        raise MyError("Too young!")

    print("Welcome!")

except MyError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")