n = int(input())

matrix = []
traveller_position = None
health = 100

for row in range(n):
    matrix.append([el for el in input()])
    for col in range(n):
        if matrix[row][col] == "P":
            traveller_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[traveller_position[0]][traveller_position[1]] = "-"
while True:
    command = input()

    move = directions[command]

    next_row = traveller_position[0] + move[0]
    next_col = traveller_position[1] + move[1]

    if not (0 <= next_row < n and 0 <= next_col < n):
        continue

    next_move = matrix[next_row][next_col]
    traveller_position = (next_row, next_col)

    if next_move == "M":
        health -= 40
        if health <= 0:
            health = 0
            break

    elif next_move == "H":
        health = min(health + 15, 100)

    matrix[next_row][next_col] = "-"

    if next_move == "X":
        break

matrix[traveller_position[0]][traveller_position[1]] = "P"

if health:
    print("Player escaped the maze. Danger passed!")
else:
    print("Player is dead. Maze over!")

print(f"Player's health: {health} units")

for row in matrix:
    print(*row, sep="")