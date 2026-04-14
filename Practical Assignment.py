#1 Fibonacci Series
print('-----Fibonacci Series------')

n = int(input("Enter number : "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\n")


#2 Sum of N Natural Numbers
print('-----Sum of N Natural Numbers------')

n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
    total += i

print("Sum =", total)
print()


#3 Series 1² + 2² + 3² + ... + n²
print('-----Sum of Squares Series------')

n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
    total += i*i

print("Sum of Squares =", total)
print()


#4 Factorial of Given Number
print('-----Factorial Program------')

n = int(input("Enter a number: "))

fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)
print()


#5 Prime Numbers Between 1 to 50
print('-----Prime Numbers (1 to 50)------')

for num in range(2, 51):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")

print("\n")


#6 Largest of 3 Numbers Using Nested If
print('-----Largest of Three Numbers------')

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest =", a)
    else:
        print("Largest =", c)
else:
    if b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)

print()


#7 List Operations
print('-----List Operations------')

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

#i. Concatenation
print("Concatenation:", list1 + list2)

#ii. Remove list1[3]
list1.remove(2000)
print("After Remove:", list1)

# iii. Add "Java" in list1
list1.append("Java")
print("After Append:", list1)

#iv. Update list2[3]=11
list2[3] = 11
print("After Update:", list2)

#v. del list2[2]
del list2[2]
print("After Delete:", list2)

#vi. Print message 4 times
for i in range(4):
    print("Welcome to Marwadi University")

#vii. Slicing
print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])

#viii. Length of list2
print("Length of list2:", len(list2))

#ix. Maximum element in list1 (numbers only)
numbers = [x for x in list1 if type(x) == int]
print("Maximum in list1:", max(numbers))

#x. Minimum element in list2
print("Minimum in list2:", min(list2))

#xi. Append 100 in list2
list2.append(100)
print("After Append 100:", list2)

#xii. Extend operation
list2.extend([200, 300])
print("After Extend:", list2)

#xiv. Difference between pop and remove
print("Using pop:", list2.pop())
list2.remove(2)
print("Using remove:", list2)

#xv. Reverse list1
list1.reverse()
print("Reverse list1:", list1)

#xvi. Sort list2 in descending order
list2.sort(reverse=True)
print("Descending list2:", list2)
