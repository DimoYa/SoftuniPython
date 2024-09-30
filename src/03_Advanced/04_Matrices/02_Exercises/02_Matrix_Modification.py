n = int(input())

matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split()])


while True:

    command_part = input().split()
    command_name = command_part[0]

    if command_name == "END":
        break

    row, col, value = [int(el) for el in command_part[1:]]

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    else:
        if command_name == "Add":
            matrix[row][col] += value
        elif command_name == "Subtract":
            matrix[row][col] -= value

for row in matrix:
    print(*row)