# Student Data Manager

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        file = open("students.txt", "a")
        file.write(roll + "," + name + "," + marks + "\n")
        file.close()

        print("Student added successfully")

    elif choice == "2":
        file = open("students.txt", "r")

        print("\nStudent Records")

        for line in file:
            print(line.strip())

        file.close()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
