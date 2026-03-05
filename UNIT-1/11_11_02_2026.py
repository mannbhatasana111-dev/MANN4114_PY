def calculate_total(*args):
    total = 0
    for num in args:
        total += num
    return total


b = []
print("Enter numbers (Type 0 to stop):")
while True:
    a = input("Enter a number: ")
    if a == "":
        print("==> Please Enter Value Don't put Empty")
        continue
    if a == "0":
        break
    else:
        b.append(int(a))
print("The sum of all numbers is : ", calculate_total(*b))
