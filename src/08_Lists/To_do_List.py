tasks = [0] * 10

command = input()

while not command == "End":
    command = command.split("-")
    priority = int(command[0]) -1
    task = command[1]

    tasks.pop(priority)
    tasks.insert(priority, task)

    command = input()

filtered_list = [task for task in tasks if not task == 0]

print(filtered_list)
