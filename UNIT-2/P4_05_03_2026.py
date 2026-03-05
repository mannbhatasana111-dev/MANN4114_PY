import calc

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting...")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            res = calc.add(num1, num2)
            print(f"Addition => {num1} + {num2} = {res}")

        elif choice == '2':
            res = calc.sub(num1, num2)
            print(f"Subtraction => {num1} - {num2} = {res}")

        elif choice == '3':
            res = calc.mul(num1, num2)
            print(f"Multiplication => {num1} * {num2} = {res}")

        elif choice == '4':
            res = calc.div(num1, num2)
            print(f"Division => {num1} / {num2} = {res}")

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Error: Please enter numbers only!")