'''
p1 = float(input("Price 1: "))
p2 = float(input("Price 2: "))

print("1.Total 2.Discount 3.Order 4.Split")
ch = int(input("Choice: "))

if ch == 1:
    print("Total =", p1 + p2)

elif ch == 2:
    d = float(input("Discount %: "))
    t = p1 + p2
    print("Final =", t - t*d/100)

elif ch == 3:
    q1 = int(input("Qty1: "))
    q2 = int(input("Qty2: "))
    print("Order Total =", p1*q1 + p2*q2)

elif ch == 4:
    n = int(input("People: "))
    print("Each Pays =", (p1+p2)/n)
'''

    

price1 = float(input("Price of first item: "))
price2 = float(input("Price of second item: "))

print("1.Total  2.Discount  3.Order  4.Split")
choice = int(input("Enter choice: "))

if choice == 1:
    print("Total Bill =", price1 + price2)

elif choice == 2:
    discount_percent = float(input("Enter discount %: "))
    total = price1 + price2
    print("Final Bill =", total - total * discount_percent / 100)

elif choice == 3:
    quantity1 = int(input("Quantity of first item: "))
    quantity2 = int(input("Quantity of second item: "))
    print("Order Total =", price1 * quantity1 + price2 * quantity2)

elif choice == 4:
    people = int(input("Number of people: "))
    print("Each Person Pays =", (price1 + price2) / people)
