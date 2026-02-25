
'''

add = lambda x, y : x + y
sub = lambda x, y : x - y
malti = lambda x, y : x * y
div = lambda x, y : x / y

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
op = input("Enter operation (+, -, *, /) : ")

if op == '+':
    print(add(num1,num2))

elif op == '-':
    print(sub(num1,num2))

elif op == '*':
    print(multi(num1,num2))

elif op == '/':
    print(div(num1,num2))

'''

