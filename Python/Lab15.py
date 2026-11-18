
students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": 2, "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": 1, "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": 1, "Marks": [74, 80, 82]}
}

while True:
    print("\n===================================")
    print("  STUDENT INFORMATION MANAGEMENT")
    print("===================================")

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = int(input("\nEnter your choice (1-7): "))

    if choice == 1:
        print("\n--- Enrolled Student Records ---")

        for roll in students:
            print("\nRoll No:", roll)
            print("Name:", students[roll]["Name"])
            print("Branch:", students[roll]["Branch"])
            print("Sem:", students[roll]["Semester"])
            print("Marks:", students[roll]["Marks"])

        print("\nTotal Enrolled Students:", len(students))

    elif choice == 2:
        roll = input("Enter Roll Number to search: ")

        if roll in students:
            print("\n[FOUND] Record for Roll No:", roll)
            print("Name:", students[roll]["Name"])
            print("Branch:", students[roll]["Branch"])
            print("Semester:", students[roll]["Semester"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("\n[NOT FOUND] Student record does not exist.")

    elif choice == 3:
        print("\n--- Register New Student ---")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("\n[ERROR] Roll Number already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            semester = int(input("Enter Semester: "))

            marks = []

            for i in range(3):
                m = int(input("Enter marks in subject " + str(i + 1) + ": "))
                marks.append(m)

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print("\n[SUCCESS] Student registered successfully.")

    elif choice == 4:
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            print("\nCurrent details for", students[roll]["Name"])
            print("1. Branch")
            print("2. Semester")

            ch = int(input("Choose field to update (1 or 2): "))

            if ch == 1:
                new = input("Enter new branch: ")
                students[roll]["Branch"] = new
                print("\n[SUCCESS] Branch updated.")

            elif ch == 2:
                new = input("Enter new semester: ")
                students[roll]["Semester"] = new
                print("\n[SUCCESS] Semester updated.")

            else:
                print("Invalid choice.")

        else:
            print("\n[NOT FOUND] Student record does not exist.")

    elif choice == 5:
        roll = input("Enter Roll Number for Academic Performance: ")

        if roll in students:
            marks = students[roll]["Marks"]

            total = sum(marks)
            average = total / len(marks)

            print("\n========== ACADEMIC REPORT ==========")
            print("Student Name:", students[roll]["Name"])
            print("Subject Marks:", marks)
            print("Total Marks:", total, "/ 300")
            print("Average Marks:", round(average, 2))

            if average >= 40:
                print("Final Result: PASS")
            else:
                print("Final Result: FAIL")

            print("=====================================")

        else:
            print("\n[NOT FOUND] Student record does not exist.")

    elif choice == 6:
        roll = input("Enter Roll Number to delete: ")

        if roll in students:
            students.pop(roll, None)
            print("\n[SUCCESS] Student record deleted successfully.")
        else:
            print("\n[NOT FOUND] Student record does not exist.")

    elif choice == 7:
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter between 1 and 7.")

