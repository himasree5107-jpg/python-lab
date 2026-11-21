# Library Management System

books = []

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully")

    elif choice == "2":
        print("\nAvailable Books")

        for book in books:
            print(book)

    elif choice == "3":
        search = input("Enter book name: ")

        if search in books:
            print("Book found")
        else:
            print("Book not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
