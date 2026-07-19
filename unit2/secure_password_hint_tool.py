"""
The Challenge: “The Secure Password Hint Tool”
Users often forget their passwords. Create a script that helps them by showing a secure hint.

1. Ask the user to input their secret password.

2. Use .strip() to clean up any accidental spaces they might have typed at the start or end.

3. Grab the very first letter and the very last letter of the password using string indexing.

4. Print a hint using an f-string that forces the letters into uppercase so they stand out.
(e.g., “Your password hint: It starts with P and ends with N”).
"""

def collect_secret() -> str:
    while True:
        secret = input("Please enter your secret password: ")
        if not secret:
            print("Password cannot be empty!")
            continue
        return secret
    return "Something went wrong when collecting your secret password"

def sanitize_password(password: str) -> str:
    if not password.strip():
        print("Password cannot be empty!")
    return password.strip()

def give_hints(password: str) -> tuple[str, str]:
    return password[0], password[-1]

def main() -> None:

    password = sanitize_password(collect_secret())
    hints = give_hints(password)

    print(f"Your Password hint: It starts with {hints[0].upper()} and ends with {hints[1].upper()}")
    print(f"Your password is {hints[0]}{'*' * (len(password)-2)}{hints[1]}")

if __name__ == "__main__":
    main()