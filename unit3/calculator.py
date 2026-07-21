"""
Task Overview
Multi-Function Calculator
Build a Python calculator called calculator.py that takes two
 numbers as input and performs all four basic arithmetic operations
 plus two advanced operations. The calculator must handle user
 input safely using type casting and display results clearly using f-strings.

Requirements
Use float(input()) to collect two numbers from the user
Calculate and display: addition, subtraction, multiplication, division
Calculate and display: floor division (//) and modulus (%)
Round all results to 2 decimal places using round()
Handle division by zero — if the second number is 0, display a friendly
error message instead of crashing
Display all results in a formatted table using f-strings


Outcome of the task
At the end of this task, you should be competent in creating and running a
Python calculator that accepts numeric user input, performs arithmetic calculations
using Python’s operators, applies type conversion, uses functions such as round() and
abs(), handles division by zero appropriately, and displays results clearly using f-strings.

Before progressing to the next unit, complete the Unit 3 Quiz to check your understanding of the key numerical operations, type conversion, and calculation concepts covered, identify any areas that may need further practice, and reinforce your learning.
"""

def collect_operants() -> tuple[float, float]:
    operand1 : float = 0.0
    operand2 : float = 0.0
    while True:
        expression = input("Enter two numbers that are operants, e.g 9.0 6.0: ")
        if not expression:
            print("You must enter two numbers separated by spaces.")
            continue

        expression = expression.split()

        try:
            operand1 = float(expression[0])
            operand2 = float(expression[1])
            break
        except ValueError:
            print("You must enter two numbers separated by spaces.")
            continue

    return operand1, operand2

def calculator(operand1: float, operand2: float) -> dict[str, float|str]:
    return {
        "addition": operand1 + operand2,
        "subtraction": operand1 - operand2,
        "multiplication": operand1 * operand2,
        "division" : operand1 / operand2 if operand2 != 0 else "Cannot divide by zero",
    }

def display(result: dict[str, float|str]) -> None:
    decorator_length = 13
    header = f"|{'*' * decorator_length }| Results |{'*' * decorator_length }|"
    print(header)
    for key, value in result.items():
        print(f"|{' ' * (int(decorator_length / 2))} -> {key.title()}: {value}")
    print(f"|{'_' * (len(header) - 2)}|")

def main() -> None:
    operands = collect_operants()
    display(calculator(operands[0], operands[1]))

if __name__ == "__main__":
    main()