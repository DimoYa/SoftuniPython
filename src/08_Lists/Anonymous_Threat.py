input_data = input().split()


while True:
    command = input()

    if command == "3:1":
        break

    command_part = command.split()
    command_name = command_part[0]
    command_parameters = command_part[1:]

    if command_name == "merge":
        input_data = merge_command(input_data, command_parameters)