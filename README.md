
**Student Management System**

## Overview of the Project

The Student Management System is a Python-based console application for managing student records and academic marks.

The project allows users to add, display, search, update, and delete student records. It also calculates total marks, percentage, and grade for a student.

Student data is stored in a JSON file so records can be saved and loaded when the program is run again.

## Features

- Add a new student
- Store student name and roll number
- Store Maths, Python, and English marks
- Display all student records
- Search for a student using roll number
- Update student details and marks
- Delete student records
- Calculate total marks
- Calculate percentage
- Calculate grade
- Check for duplicate roll numbers
- Save and load student data using JSON
- Menu-driven console interface

## Technologies / Tools Used

- **Programming Language:** Python 3
- **Data Storage:** JSON
- **Python Library:** `json`
- **IDE/Editor:** VS Code, PyCharm, IDLE, or any Python-supported editor
- **Version Control:** Git and GitHub

## Steps to Install & Run the Project

### 1. Install Python

Install Python 3 or later.

Check the installation:

```bash
python --version
```

### 2. Download or Clone the Project

Download the project files or clone the GitHub repository.

### 3. Open the Project Folder

Open the folder in VS Code, PyCharm, IDLE, or another Python-supported editor.

### 4. Run the Project

Open the terminal inside the project folder and run:

```bash
python main.py
```

### 5. Use the Menu

The program displays:

```text
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Result
7. Exit
```

Enter the number corresponding to the required operation.

## Instructions for Testing

### Test 1: Add Student

1. Select option `1`.
2. Enter the student's name.
3. Enter the roll number.
4. Enter Maths, Python, and English marks.
5. Verify that the student is added successfully.

### Test 2: Display Students

1. Select option `2`.
2. Verify that all saved student records are displayed.

### Test 3: Search Student

1. Select option `3`.
2. Enter an existing roll number.
3. Verify that the correct student's details are displayed.
4. Try a non-existing roll number and verify the `Student not found!` message.

### Test 4: Update Student

1. Select option `4`.
2. Enter an existing roll number.
3. Enter the updated details and marks.
4. Verify that the information is updated.

### Test 5: Delete Student

1. Select option `5`.
2. Enter an existing roll number.
3. Verify that the student record is deleted.

### Test 6: Calculate Result

1. Select option `6`.
2. Enter an existing roll number.
3. Verify the total marks, percentage, and grade.

### Test 7: Duplicate Roll Number

1. Select option `1`.
2. Enter a roll number that already exists.
3. Verify that `Roll number already exists!` is displayed.

### Test 8: Exit

1. Select option `7`.
2. Verify that the program exits successfully.



## Project Structure

```text
Student_Management_System/
│
├── main.py
├── data.py
├── storage.py
├── student_operations.py
├── result.py
└── students.json
```

### File Description

- **main.py** – Main menu and program execution.
- **data.py** – Shared student data list.
- **storage.py** – Loads and saves student data using JSON.
- **student_operations.py** – Add, display, search, update, and delete operations.
- **result.py** – Calculates total marks, percentage, and grade.
- **students.json** – Stores student records.
