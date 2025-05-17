message = input()
command = input()


def move_command(m, params):
    n = int(params[0])
    return m[n:] + m[:n]


def insert_command(m, params):
    index, value = int(params[0]), params[1]
    return m[:index] + value + m[index:]


def change_all_command(m, params):
    substring, replacement = params[0], params[1]
    return m.replace(substring, replacement)


while not command == "Decode":
    token = command.split("|")
    command_name = token[0]
    command_params = token[1:]

    if command_name == "Move":
        message = move_command(message, command_params)
    elif command_name == "Insert":
        message = insert_command(message, command_params)
    elif command_name == "ChangeAll":
        message = change_all_command(message, command_params)

    command = input()
print(f"The decrypted message is: {message}")