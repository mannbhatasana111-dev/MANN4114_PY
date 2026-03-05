try:
    with open("numbers.txt", "r") as file:
        data = file.read().split()
        numbers = [float(x) for x in data]
    if not numbers:
        print("The file is empty!")
    else:
        total = sum(numbers)
        maximum = max(numbers)
        minimum = min(numbers)

        print(f"Numbers found: {numbers}")
        print("-" * 20)
        print(f"Total Sum : {total}")
        print(f"Maximum   : {maximum}")
        print(f"Minimum   : {minimum}")

except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
except ValueError:
    print("Error: The file contains non-numeric characters.")