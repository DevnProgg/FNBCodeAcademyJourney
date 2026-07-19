"""
Create a program that acts as a digital ticket counter.
1. Ask the user for their name.

2. Ask them for the name of the band/artist they want to see.

3. Print a personalized confirmation message using an f-string that
says something like: “Hey [Name]! Your tickets to see [Artist] are booked successfully!”
"""

def collect_name() -> str:
    return input("Please Enter your name: ")

def collect_band_name() -> str:
    return input("Please Enter the band/artist you want to see: ")

def main() -> None:
    print("Welcome to the Concert Ticket Booker!")
    print(f"Hey {collect_name()}! Your tickets to see {collect_band_name()} are booked successfully!")

if __name__ == "__main__":
    main()