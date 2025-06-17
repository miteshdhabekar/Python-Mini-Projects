shopping_cart = []

while True:
    print("shopping list")
    print("1. Add item")
    print("2. Remove item")
    print("3. View item")
    print("4. Clear item")
    print("5. Exit")
    choice = input("Enter your choice for shopping")
    if choice == "1":
        item = input("enter the item")
        shopping_cart.append(item)
        print(f"{item} is been added")
    elif choice == "2":
        item = input("enter the item to be removed")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f"{item} is been removed")
        else:
            print(f"{item} doesn't exist in the cart")
    elif choice == "3":
        if not shopping_cart:
            print("empty")
        else:
            for item in shopping_cart:
                print(item)
    elif choice =="4":
        shopping_cart.clear()
        print("The item in the cart are empty now")
    elif choice == "5":
        print("end my shopping")
        print("restart your shopping")
        break
    else:
        print("invalid choice")