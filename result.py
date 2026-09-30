from data import students


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
