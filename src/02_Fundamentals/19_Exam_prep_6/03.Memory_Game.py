elements = [el for el in input().split()]

command = input()
turns = 0

while not command == "end" and elements:
    index1, index2 = [int(el) for el in command.split()]
    turns += 1

    if index1 == index2 or index1 < 0 or index1 >= len(elements) or index2 < 0 or index2 >= len(elements):
        mid = len(elements) // 2
        elements = elements[:mid] + [f"-{turns}a", f"-{turns}a"] + elements[mid:]
        print("Invalid input! Adding additional elements to the board")
        command = input()
        continue

    if elements[index1] == elements[index2]:
        value_to_remove = elements[index1]
        print(f"Congrats! You have found matching elements - {value_to_remove}!")

        elements = [el for el in elements if el != value_to_remove]
    else:
        print("Try again!")


    command = input()

if elements:
    print("Sorry you lose :(")
    print(' '.join([str(el) for el in elements]))
else:
    print(f"You have won in {turns} turns!")