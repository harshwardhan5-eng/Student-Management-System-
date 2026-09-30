from data import students
from storage import save_students


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
