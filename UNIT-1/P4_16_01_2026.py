# Armstrong number check for 10 numbers

def is_armstrong(nm):
    n = len(str(nm))
    a = nm
    sum_val = 0
    while a > 0:
        digit = a % 10
        sum_val += digit ** n
        a //= 10
    return sum_val == nm

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is NOT an Armstrong number")
