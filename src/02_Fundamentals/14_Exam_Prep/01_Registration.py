username = input()
command = input()


def letters_command(usr, command_parameters):
    lower_or_upper = command_parameters[0]

    if lower_or_upper == "Lower":
        usr = usr.lower()
    else:
        usr = usr.upper()

    print(usr)
    return usr


def reverse_command(usr, command_parameters):
    start_index = int(command_parameters[0])
    end_index = int(command_parameters[1])

    if 0 <= start_index < len(usr) and 0 < end_index <= len(usr):
        substr = usr[start_index:end_index + 1]
        reversed_string = substr[::-1]

        print(reversed_string)
    return usr


def substring_command(usr, command_parameters):
    substr = command_parameters[0]
    if substr in usr:
        usr = usr.replace(substr, "")
        print(usr)
    else:
        print(f"The username {usr} doesn't contain {substr}.")
    return usr


def replace_command(usr, command_parameters):
    substr = command_parameters[0]
    usr = usr.replace(substr, "-")
    print(usr)
    return usr


def is_valid_command(usr, command_parameters):
    substr = command_parameters[0]

    if substr in usr:
        print("Valid username.")
    else:
        print(f"{substr} must be contained in your username.")
    return usr


while not command == "Registration":

    token = command.split()

    command_name = token[0]
    command_parameters = token[1:]

    if command_name == "Letters":
        username = letters_command(username, command_parameters)
    elif command_name == "Reverse":
        username = reverse_command(username, command_parameters)
    elif command_name == "Substring":
        username = substring_command(username, command_parameters)
    elif command_name == "Replace":
        username = replace_command(username, command_parameters)
    elif command_name == "IsValid":
        username = is_valid_command(username, command_parameters)
    command = input()
