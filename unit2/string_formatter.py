"""
Task Overview
Username and Message Formatter
Write a Python script called string_formatter.py that takes a user’s first name,
last name, and a short bio message as input, then applies multiple string transformations
to produce a formatted user profile output. This simulates how a real app backend processes
 user-submitted text.

Requirements
Collect first name, last name, and bio message using input()
Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
Display the full name in Title Case using .title()
Strip leading/trailing whitespace from the bio before displaying it using .strip()
Count and display the number of characters in the bio using len()
Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
Display all output using f-strings
"""

#utils
def text_field(placeholder: str) -> str:
    while True:
        data : str = input(f"-> {placeholder} :")
        if not data:
            continue
        return data.strip()
    return "Something went wrong"

def generate_username(first_name: str, last_name: str) -> str:
    first_name_initial = first_name[0].lower()
    username = first_name_initial + last_name.lower()
    return username

def sanitize_bio(bio: str) -> str:
    bio = bio.replace("I am", "I'm")

    return bio

def display(first_name: str, last_name: str, bio_message: str) -> None:
    print(f"Full name: {first_name.title()} {last_name.title()}")
    print(f"Bio message: {bio_message} \n count: {len(bio_message)}")

def main() -> None:
        firstname = text_field("First Name")
        lastname = text_field("Last Name")
        bio = text_field("Bio")

        username = generate_username(firstname, lastname)
        bio = sanitize_bio(bio)
        display(firstname, lastname, bio)

if __name__ == "__main__":
    main()