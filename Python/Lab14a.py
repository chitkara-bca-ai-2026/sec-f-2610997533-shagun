books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert Martin", "2008", "Software Engineering")
]

library_categories = set()

for book in books:
    library_categories.add(book[3])

student_wishlist = {
    "AI", "Cloud Computing", "Robotics", "Cybersecurity"
}

while True:

    print("\n===== LIBRARY BOOK MANAGER =====")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Categories")
    print("4. Add Category to Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:

        print("\n--- Library Books ---")

        for book in books:
            title, author, year, category = book

            print("Title:", title)
            print("Author:", author)
            print("Year:", year)
            print("Category:", category)
            print()

    elif choice == 2:

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category: ")

        new_book = (title, author, year, category)

        books.append(new_book)
        library_categories.add(category)

        print("Book added successfully!")

    elif choice == 3:

        print("\n--- Unique Categories ---")

        for category in library_categories:
            print(category)

    elif choice == 4:

        category = input("Enter category: ")

        student_wishlist.add(category)

        print("Category added to wishlist!")

    elif choice == 5:

        common = set()
        missing = set()
        all_categories = set()

       
        for category in library_categories:
            if category in student_wishlist:
                common.add(category)

        
        for category in student_wishlist:
            if category not in library_categories:
                missing.add(category)

        
        for category in library_categories:
            all_categories.add(category)

        for category in student_wishlist:
            all_categories.add(category)

        print("\nCommon Categories:", common)
        print("Missing Categories:", missing)
        print("All Categories:", all_categories)

    elif choice == 6:

        print("Thank you!")
        break

    else:

        print("Invalid choice!")
