n = int(input())

matrix = []
jet_position = None
armor_value = 300
damage = 100
enemies = 0

for row in range(n):
    line = [x for x in input()]
    matrix.append(line)
    for col in range(n):
        if matrix[row][col] == "J":
            jet_position = (row, col)
        if matrix[row][col] == "E":
            enemies += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[jet_position[0]][jet_position[1]] = "-"

while True:
    command = input()

    move = directions[command]

    # Calculate next position
    next_row = jet_position[0] + move[0]
    next_col = jet_position[1] + move[1]

    next_move = matrix[next_row][next_col]

    if next_move == "E":
        armor_value -= damage
        enemies -= 1

    if next_move == "R":
        armor_value = 300

    matrix[next_row][next_col] = "-"
    jet_position = (next_row, next_col)

    if armor_value == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
        break
    if enemies == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
        break

matrix[jet_position[0]][jet_position[1]] = "J"

for row in matrix:
    print(*row, sep="")
