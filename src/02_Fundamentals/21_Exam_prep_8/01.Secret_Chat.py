secret = input()
command = input()


def insert_command(command_params, secret):
    index = int(command_params[0])
    return secret[:index] + " " + secret[index:]


def reverse_command(command_params, secret):
    substring = command_params[0]

    if substring not in secret:
        print("error")
        return None  # signal failure

    start_index = secret.find(substring)
    end_index = start_index + len(substring)
    reversed_part = substring[::-1]

    new_secret = secret[:start_index] + reversed_part + secret[end_index:]
    return new_secret


def change_all_command(command_params, secret):
    substring = command_params[0]
    replacement = command_params[1]
    return secret.replace(substring, replacement)


while command != "Reveal":
    token = command.split(":|:")
    command_name = token[0]
    command_parameters = token[1:]

    new_secret = None
    if command_name == "InsertSpace":
        new_secret = insert_command(command_parameters, secret)
    elif command_name == "Reverse":
        new_secret = reverse_command(command_parameters, secret)
    elif command_name == "ChangeAll":
        new_secret = change_all_command(command_parameters, secret)

    if new_secret is not None:
        secret = new_secret
        print(secret)

    command = input()

print(f"You have a new text message: {secret}")
