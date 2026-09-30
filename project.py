import json

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    
    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll number already exists!")
            return

    math = float(input("Enter Maths marks: "))
    python = float(input("Enter Python marks: "))
    english = float(input("Enter English marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "math": math,
        "python": python,
        "english": english
    }

    students.append(student)

    save_students()

    print("Student added successfully!")


def display_students():

    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== ALL STUDENTS =====")

    for student in students:

        print("\nName:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Maths:", student["math"])
        print("Python:", student["python"])
        print("English:", student["english"])


def search_student():

    roll_no = input("Enter roll number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\n===== STUDENT FOUND =====")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Maths:", student["math"])
            print("Python:", student["python"])
            print("English:", student["english"])

            return

    print("Student not found!")


def update_student():

    roll_no = input("Enter roll number to update: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent found!")

            student["name"] = input("Enter new name: ")
            student["math"] = float(input("Enter new Maths marks: "))
            student["python"] = float(input("Enter new Python marks: "))
            student["english"] = float(input("Enter new English marks: "))

            save_students()

            print("Student updated successfully!")

            return

    print("Student not found!")


def delete_student():

    roll_no = input("Enter roll number to delete: ")

    for student in students:

        if student["roll_no"] == roll_no:

            students.remove(student)

            save_students()

            print("Student deleted successfully!")

            return

    print("Student not found!")


def calculate_result():

    roll_no = input("Enter roll number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            total = (
                student["math"]
                + student["python"]
                + student["english"]
            )

            percentage = total / 3

            if percentage >= 90:
                grade = "A+"

            elif percentage >= 80:
                grade = "A"

            elif percentage >= 70:
                grade = "B"

            elif percentage >= 60:
                grade = "C"

            elif percentage >= 50:
                grade = "D"

            else:
                grade = "F"

            print("\n===== RESULT =====")

            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Total Marks:", total)
            print("Percentage:", percentage, "%")
            print("Grade:", grade)

            return

    print("Student not found!")

students = load_students()


while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Result")
    print("7. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_result()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")