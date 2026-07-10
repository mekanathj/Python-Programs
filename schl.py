students = []

def add_student():
    """Add a new student record."""
    try:
        roll = int(input("Enter Roll Number: "))
        for s in students:
            if s['roll'] == roll:
                print("❌ Roll number already exists!")
                return
        name = input("Enter Name: ").strip()
        grade = input("Enter Grade/Class: ").strip()
        students.append({"roll": roll, "name": name, "grade": grade})
        print("✅ Student added successfully!")
    except ValueError:
        print("❌ Invalid input! Roll number must be an integer.")

def view_students():
    """Display all student records."""
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Grade: {s['grade']}")
    print("-----------------------")

def search_student():
    """Search for a student by roll number."""
    try:
        roll = int(input("Enter Roll Number to search: "))
        for s in students:
            if s['roll'] == roll:
                print(f"✅ Found: Roll: {s['roll']}, Name: {s['name']}, Grade: {s['grade']}")
                return
        print("❌ Student not found.")
    except ValueError:
        print("❌ Invalid input! Roll number must be an integer.")

def delete_student():
    """Delete a student by roll number."""
    try:
        roll = int(input("Enter Roll Number to delete: "))
        for s in students:
            if s['roll'] == roll:
                students.remove(s)
                print("✅ Student deleted successfully!")
                return
        print("❌ Student not found.")
    except ValueError:
        print("❌ Invalid input! Roll number must be an integer.")

while True:
    print("\n===== School Records Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 5.")
