from collections import deque

quantity = int(input())
name = input()
names = deque([])

while not name == "Start":
    names.append(name)
    name = input()

command = input()

while not command == "End":

    if command.isdigit():
        litters = int(command)
        current_person = names.popleft()

        if quantity >= litters:
            quantity -= litters
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait" )
    else:
        command = command.split()
        _, litters = command
        litters = int(litters)
        quantity += litters

    command = input()
print(f"{quantity} liters left", end="")

