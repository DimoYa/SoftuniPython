def contains_command(list_params, key):
    substr = list_params[0]

    if not substr in key:
        print("Substring not found!")
    else:
        print(f"{key} contains {substr}")

def flip_command(list_params, key):
    case_direction = list_params[0]
    start_index = int(list_params[1])
    end_index = int(list_params[2])

    substring = key[start_index:end_index]

    if case_direction == "Upper":
        flipped = substring.upper()
    else:
        flipped = substring.lower()

    result = key[:start_index] + flipped + key[end_index:]
    return result

def slice_command(list_params, key):
    start_index = int(list_params[0])
    end_index = int(list_params[1])

    substring = key[start_index:end_index]

    result = key.replace(substring, "")
    return result


activation_key = input()

command = input()

while not command == "Generate":
    token = command.split(">>>")
    command_name = token[0]
    parameters = token[1:]

    if command_name == "Contains":
        contains_command(parameters, activation_key)
    elif command_name == "Flip":
        activation_key = flip_command(parameters, activation_key)
        print(activation_key)
    elif command_name == "Slice":
        activation_key = slice_command(parameters, activation_key)
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")