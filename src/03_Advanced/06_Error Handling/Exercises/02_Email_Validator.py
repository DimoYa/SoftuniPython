class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


ADD_SYMBOL = "@"
MINIMAL_USR_SYMBOL = 4
VALID_TLDS = ["com", "bg", "org", "net"]


email = input()

while not email == "End":

    if ADD_SYMBOL not in email:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = email.split("@")
    domain_name, tld = domain.split(".")

    if len(username) <= MINIMAL_USR_SYMBOL:
        raise NameTooShortError("Name must be more than 4 characters")

    if tld not in VALID_TLDS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
