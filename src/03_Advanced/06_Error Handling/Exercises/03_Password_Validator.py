import re

class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

MINIMUM_PASS_CHARS = 8

while True:
    password = input()

    if password == "Done":
        break

    if len(password) < MINIMUM_PASS_CHARS:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if not re.search(r"[a-zA-Z]", password) or not re.search(r"[0-9]", password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
