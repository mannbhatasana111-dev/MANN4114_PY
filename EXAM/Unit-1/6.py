code = input("Enter artifact code: ")

if code == code[::-1]:
    print("It is a Palindrome Code")
else:
    print("It is Not a Palindrome Code")

'''
A palindrome code reads the same forward and backward.
The program checks if the code is equal to its reverse.
If both are the same, the artifact code is identified as a palindrome.
'''
