activation_key = input()

command = input()


def contains_command(params):
    substring = params[0]

    if substring not in activation_key:
        print("Substring not found!")
        return
    print(f"{activation_key} contains {substring}")


def flip_command(params):
    direction, start_index, end_index = params
    start_index = int(start_index)
    end_index = int(end_index)

    substring = activation_key[start_index:end_index]

    if direction == "Upper":
        result = str.replace(activation_key, substring, str.upper(substring))
    else:
        result = str.replace(activation_key, substring, str.lower(substring))
    print(result)
    return result


def slice_command(params):
    start_index, end_index = params
    start_index = int(start_index)
    end_index = int(end_index)

    substring = activation_key[start_index:end_index]

    result = str.replace(activation_key, substring, "")
    print(result)
    return result


while command != "Generate":
    token = command.split(">>>")

    command_name = token[0]
    command_params = token[1:]

    if command_name == "Contains":
        contains_command(command_params)
    elif command_name == "Flip":
        activation_key = flip_command(command_params)
    elif command_name == "Slice":
        activation_key = slice_command(command_params)



    command = input()

print(f"Your activation key is: {activation_key}")

    