import json
from data import students

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
