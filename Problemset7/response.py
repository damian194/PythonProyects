import validators

def is_valid_email(email):
    if not validators.email(email):
        return False

    if email.count('@') != 1:
        return False

    username, domain = email.split('@')
    if not username or not domain:
        return False

    if not username.isalnum() or not all(c.isalnum() or c in ['.', '-', '_'] for c in domain):
        return False

    return True

def main():
    email = input("Enter an email address: ")

    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
