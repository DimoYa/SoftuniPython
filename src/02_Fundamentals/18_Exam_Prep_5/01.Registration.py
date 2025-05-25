desired_username = input()
command = input()


def letters_command(command_parameters):
    case = command_parameters[0]

    if case == "Lower":
        result = desired_username.lower()
    else:
        result = desired_username.upper()

    print(result)
    return result


def reverse_command(command_parameters):
    start_index = int(command_parameters[0])
    end_index = int(command_parameters[1])

    if 0 <= start_index <= end_index < len(desired_username):
        substring = desired_username[start_index:end_index + 1]
        print(substring[::-1])
    else:
        # Optional: you could give feedback if indices are invalid
        pass


def substring_command(command_parameters):
    substring = command_parameters[0]

    if substring in desired_username:
        result = desired_username.replace(substring, "")
        print(result)
        return result
    else:
        print(f"The username {desired_username} doesn't contain {substring}.")
        return desired_username  # Return original if not found


def replace_command(command_parameters):
    char = command_parameters[0]
    result = desired_username.replace(char, "-")
    print(result)
    return result


def isvalid_command(command_parameters):
    char = command_parameters[0]

    if char in desired_username:
        print("Valid username.")
    else:
        print(f"{char} must be contained in your username.")


while command != "Registration":
    token = command.split()
    command_name = token[0]
    command_parameters = token[1:]

    if command_name == "Letters":
        desired_username = letters_command(command_parameters)
    elif command_name == "Reverse":
        reverse_command(command_parameters)
    elif command_name == "Substring":
        desired_username = substring_command(command_parameters)
    elif command_name == "Replace":
        desired_username = replace_command(command_parameters)
    elif command_name == "IsValid":
        isvalid_command(command_parameters)

    command = input()