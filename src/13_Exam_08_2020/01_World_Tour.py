def add_stop_command(command_parameters, original_string):
    index = int(command_parameters[0])
    to_insert = command_parameters[1]

    if 0 <= index <= len(original_string):
        original_string = original_string[:index] + to_insert + original_string[index:]

    return original_string


def remove_stop_command(command_parameters, original_string):
    start_index = int(command_parameters[0])
    end_index = int(command_parameters[1])

    if 0 <= start_index <= end_index < len(original_string):
        original_string = original_string[:start_index] + original_string[end_index + 1:]

    return original_string


def switch_command(command_parameters, original_string):
    old_string = command_parameters[0]
    new_string = command_parameters[1]

    if old_string in original_string:
        original_string = original_string.replace(old_string, new_string)

    return original_string


stops = input()
commands = input()

while not commands == "Travel":
    command_line = commands.split(":")
    command = command_line[0]
    command_parameters = command_line[1:]

    if command == "Add Stop":
        stops = add_stop_command(command_parameters, stops)
    elif command == "Remove Stop":
        stops = remove_stop_command(command_parameters, stops)
    elif command == "Switch":
        stops = switch_command(command_parameters, stops)

    print(stops)
    commands = input()

print(f"Ready for world tour! Planned stops: {stops}")

