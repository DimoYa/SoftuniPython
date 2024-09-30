class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin, initial_balance, age = input().split(", ")
pin = int(pin)
initial_balance = float(initial_balance)
age = int(age)
MINIMUM_LEGAL_AGE = 18

command = input()

while not command == "End":

    command_parts = command.split("#")

    command_name = command_parts[0]

    if command_name == "Send Money":
        money = float(command_parts[1])
        pin_code = int(command_parts[2])

        if money > initial_balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")

        if age < MINIMUM_LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        print(f"Successfully sent {money:.2f} money to a friend")
        initial_balance -= money
        print(f"There is {initial_balance:.2f} money left in the bank account")

    elif command_name == "Receive Money":
        money = float(command_parts[1])

        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        initial_balance += money / 2

        print(f"{(money / 2):.2f} money went straight into the bank account")

    command = input()
