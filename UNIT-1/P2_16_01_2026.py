# Calculation Opration

print(' + , - , * , / ')
op=input("Enter the Operation : ")
oplist = ['+', '-', '*', '/']
if op in oplist:
    a=int(input("Enter the Number : "))
    b=int(input("Enter the Number : "))
    if  op == '+':
        print(a,'+',b,'=',a+b)
    elif op == '-':
        print(a,'-',b,'=',a-b)
    elif op == '*':
        print(a,'*',b,'=',a*b)
    elif op == '/':
        print(a,'/',b,'=',a/b)
else:
    print('Operation Not Supported')