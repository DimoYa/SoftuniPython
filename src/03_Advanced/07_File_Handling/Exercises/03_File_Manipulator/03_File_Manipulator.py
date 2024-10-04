import os

while True:
    command = input()
    if command == "End":
        break

    command_name, file_name, *args = command.split("-")

    if command_name == "Create":
        open(file_name, "w").close()
    elif command_name == "Add":
        with open(file_name, "a") as f:
            f.write(f"{args[0]}\n")
    elif command_name == "Replace":
        content = ""
        try:
            with open(file_name, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print("An error occurred")
        else:
            content = content.replace(args[0], args[1])
            with open(file_name, "w") as f:
                f.write(content)
    elif command_name == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
