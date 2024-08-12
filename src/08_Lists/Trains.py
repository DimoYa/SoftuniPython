def add_command(wagons, command_arguments):
    people = int(command_arguments[0])

    wagons[-1] += people
    return wagons


def insert_command(wagons, command_arguments):
    index = int(command_arguments[0])
    people = int(command_arguments[1])

    wagons[index] += people
    return wagons


def leave_command(wagons, command_arguments):
    index = int(command_arguments[0])
    people = int(command_arguments[1])

    wagons[index] -= people
    return wagons


number_of_wagons = int(input())
wagons = [0] * number_of_wagons

command = input()

while not command == "End":
    command = command.split()
    command_name = command[0]
    command_arguments = command[1:]

    if command_name == "add":
        wagons = add_command(wagons, command_arguments)
    elif command_name == "insert":
        wagons = insert_command(wagons, command_arguments)
    elif command_name == "leave":
        wagons = leave_command(wagons, command_arguments)

    command = input()

print(wagons)
