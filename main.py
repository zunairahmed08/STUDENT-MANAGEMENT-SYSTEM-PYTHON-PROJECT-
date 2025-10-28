# -----------------------------------------------
# 🎓 Student Management System (Python Project)
# -----------------------------------------------

# ✅ Load existing student data from file
def load_students():
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                students.append({"name": name, "roll": roll, "marks": marks})
    except FileNotFoundError:
        pass
    return students

# ✅ Save student data into file
def save_students(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['roll']},{s['marks']}\n")

# ✅ Menu display function
def menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

# Load previous data (if file exists)
students = load_students()

# ✅ Function to add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    students.append({"name": name, "roll": roll, "marks": marks})
    save_students(students)
    print("✅ Student added successfully!\n")

# ✅ Function to view all students
def view_students():
    if not students:
        print("No students found!\n")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()

# ✅ Function to search by roll number
def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"✅ Found: {s['name']} - Marks: {s['marks']}\n")
            return
    print("❌ Student not found!\n")

# ✅ Function to update marks
def update_marks():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s['roll'] == roll:
            new_marks = input("Enter new marks: ")
            s['marks'] = new_marks
            save_students(students)
            print("✅ Marks updated successfully!\n")
            return
    print("❌ Student not found!\n")

# ✅ Function to delete a student
def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            save_students(students)
            print("✅ Student deleted!\n")
            return
    print("❌ Student not found!\n")

# ✅ Main loop to run the menu
while True:
    menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting program... Have a nice day!")
        break
    else:
        print("❌ Invalid choice, please try again!\n") 