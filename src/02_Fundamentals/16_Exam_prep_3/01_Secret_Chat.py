message = input()
command = input()


def insert_space_command(s, commands):
    index = int(commands[0])
    s = s[:index] + " " + s[index:]
    print(s)
    return s


def reverse_command(s, commands):
    substring = commands[0]

    if substring not in s:
        print("error")
    else:
        s = s.replace(substring, "", 1)
        reversed_s = substring[::-1]
        s = s + reversed_s
        print(s)
    return s


def change_all_command(s, commands):
    substring = commands[0]
    replacement = commands[1]
    s = s.replace(substring, replacement)
    print(s)
    return s


while not command == "Reveal":

    token = command.split(":|:")
    command_name = token[0]
    command_params = token[1:]

    if command_name == "InsertSpace":
        message = insert_space_command(message, command_params)
    elif command_name == "Reverse":
        message = reverse_command(message, command_params)
    elif command_name == "ChangeAll":
        message = change_all_command(message, command_params)

    command = input()

print(f"You have a new text message: {message}", end="")
