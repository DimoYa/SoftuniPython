activation_key = input()
command = input()


def contains_command(key, commands):
    substring = commands[0]

    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")


def flip_command(key, commands):
    is_lower_upper = commands[0]
    start_index = int(commands[1])
    end_index = int(commands[2])
    substring = key[start_index:end_index]

    if is_lower_upper == "Lower":
        key = key.replace(substring, substring.lower())
    else:
        key = key.replace(substring, substring.upper())

    print(key)
    return key


def slice_command(key, commands):
    start_index = int(commands[0])
    end_index = int(commands[1])
    substring = key[start_index:end_index]
    key = key.replace(substring, "")
    print(key)
    return key


while not command == "Generate":
    token = command.split(">>>")
    command_name = token[0]
    command_parameters = token[1:]

    if command_name == "Contains":
        contains_command(activation_key, command_parameters)
    elif command_name == "Flip":
        activation_key = flip_command(activation_key, command_parameters)
    elif command_name == "Slice":
        activation_key = slice_command(activation_key, command_parameters)

    command = input()

print(f"Your activation key is: {activation_key}")