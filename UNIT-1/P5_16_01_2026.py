# Odd Even number check for 10 numbers

def check_odd(n):
    if n % 2 != 0:
        return True
    return None

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

odd_numbers = []
for num in numbers:
   if check_odd(num):
       odd_numbers.append(num)

print(odd_numbers)
print(max(odd_numbers),'is largest Odd Number')