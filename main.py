from data import students
from storage import load_students

from student_operations import (
    add_student,
    display_students,
    search_student,
    update_student,
    delete_student
)

from result import calculate_result


students.extend(load_students())


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
