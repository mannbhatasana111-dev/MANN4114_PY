principal = float(input("Enter savings amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter investment duration (years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
print("Total Amount =", principal + simple_interest)
