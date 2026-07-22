"""
The Challenge: “The South African Fuel Cost Calculator”
With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:

1. Ask the user how many kilometers they want to drive.

2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).

3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
(Formula: liters_needed = kilometers / 10).

4. Calculate the total cost (liters_needed * petrol_price).

5. Use type casting to ensure your numbers work, and use round() to format the
final cost to 2 decimal places.
"""
#write simple code from now on that just solves the problem statement
def display()->None:
    MAX_SPACER : int = 20
    title = " [ Fuel Calculator ] "
    error : str | None = None
    kilometers : float= 0.0
    while True:
        print(f"+{'-' * 20}{title}{'-' * 20}")
        print(f"|{MAX_SPACER * ' '} Error: {error} {MAX_SPACER * ' '}|" if error else " ")
        kms = input(f"|{MAX_SPACER * ' '} Enter The Kilometers You want to drive: ")
        if not kms:
            error = "Kilometers Not Available, Try Again!"
            continue
        try:
            kilometers = float(kms)
            break
        except ValueError:
            error = "Kilometers Not Available, Try Again!"
            continue

def main() -> None:

if __name__ == '__main__':