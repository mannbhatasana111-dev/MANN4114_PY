a=[]
def show_list():
    print(a,"\n")
val = True
while val:
    print("1.Add Elements")
    print("2.Remove Elements")
    print("3.Sort List")
    print("4.Print List")
    print("5.Search Elements")
    print("6.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a.append(int(input("Enter a number: ")))
        print("Element Added")
        show_list()
    elif choice == 2:
        a.remove(int(input("Enter a number: ")))
        print("Element Deleted")
        show_list()
    elif choice == 3:
        a.sort()
        show_list()
    elif choice == 4:
        show_list()
    elif choice == 5:
        se = int(input("Enter a Searching number: "))
        if se in a:
            print("ELement in List\n")
        else:
            print("Element Not in List\n")
    elif choice == 6:
        break
    else:
        print("Enter a valid choice\n")
        val = True
