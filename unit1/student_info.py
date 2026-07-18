"""
Task Overview
Student Info Formatter
Write a Python script called student_info.py that collects personal information from
the user and displays it in a formatted profile card. The program must demonstrate correct
use of all four data types, string manipulation, arithmetic, and the f-string output format.

Requirements
Use input() to collect: first name, surname, age (as an integer), and a
favourite number (as a float)
Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
Display the name in UPPERCASE using .upper() and in Title Case using .title()
Calculate and display the age in months (age × 12)
Round the favourite number to 2 decimal places using round()
Print the data type of each collected value using type()
"""
import logging
# import subprocess
# import os

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

CARD_WIDTH = 113
LEFT_PADDING = 5

#TODO: figure out why clear screen is not working on my system
def clear_screen() -> None:
    # command = 'cls' if os.name == 'nt' else 'clear'
    # subprocess.run(command, shell=True)
    return

def card_spacer(height : int = 1) -> None:
    for h in range(height):
        print("|                                                                                                                 | ")
def info_field(info: str) -> None:
    content = " " * LEFT_PADDING + info

    if len(content) > CARD_WIDTH:
        content = content[:CARD_WIDTH]

    print(f"|{content:<{CARD_WIDTH}}|")

def collect_student_info() -> dict[str, str | int | float] | None:
    while True:
        first_name = input("Enter your first name: ")
        if not first_name:
            print("Error: Make sure you enter full name")
            clear_screen()
            break

        surname = input("Enter your surname: ")
        if not surname:
            print("Error: Make sure you enter surname")
            clear_screen()
            break
        try:
            age = int(input("Enter your age: "))
        except Exception as exc:
            print("Error: Make sure you enter age")
            logger.error(exc)
            clear_screen()
            break
        try:
            favourite_number = float(input("Enter your favourite number: "))
        except Exception as exc:
            print("Error: Make sure you enter favourite number ")
            logger.error(exc)
            clear_screen()
            break

        age_in_months = age * 12
        return {
            "first_name": first_name,
            "surname": surname,
            "age": age_in_months,
            "favourite_number": favourite_number
        }
    return None


def display_student_info(student_info: dict[str, str | int | float]) -> None:
    print("|---------------------------------------------| Student Information Card |----------------------------------------| ")
    card_spacer()

    info_field(f"First Name -> {student_info.get("first_name", "404 - NotFound")} Type {type(student_info.get("first_name"))}")
    info_field(f"Surname -> {student_info.get("surname", "404 - NotFound")} Type {type(student_info.get("surname"))}")
    info_field(f"Age -> {student_info.get("age", "404 - NotFound")} Type {type(student_info.get("age"))}")
    info_field(f"Fav Number -> {student_info.get("favourite_number", "404 - Not Found")} Type {type(student_info.get("favourite number"))}")
    card_spacer()
    print("|-----------------------------------------------------------------------------------------------------------------| ")


def main():
    print("<-------------------------------| Welcome to the Student Profile Form |--------------------------->")
    student_info = collect_student_info()
    while not student_info:
        student_info = collect_student_info()

    clear_screen()
    display_student_info(student_info)

if __name__ == "__main__":
    main()