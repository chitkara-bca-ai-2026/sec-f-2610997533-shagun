
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:

    print("\n===== INVENTORY CONTROL SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = int(input("\nEnter your choice (1-5): "))

    if choice == 1:

        print("\n--- Current Inventory ---")

        for item in inventory:
            print(item)

    elif choice == 2:

        item = input("Enter item name to add: ")

        inventory.append(item)

        print(item, "added to inventory.")

    elif choice == 3:

        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print(item, "removed from inventory.")
        else:
            print("Item not found in inventory.")

    elif choice == 4:

        inventory.sort()

        print("Inventory sorted alphabetically.")

        for item in inventory:
            print(item)

    elif choice == 5:

        print("Thank you for using Inventory Control System!")
        break

    else:

        print("Invalid choice! Please enter a number from 1 to 5.")
