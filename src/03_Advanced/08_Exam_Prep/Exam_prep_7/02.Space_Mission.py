n = int(input())
matrix = []
spaceship_position  = None
resources = 100
mission_status = None  # "won", "failed", "lost"

for row in range(n):
    line = input().split()
    matrix.append([el for el in line])
    if "S" in line:
        spaceship_position = row, line.index("S")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[spaceship_position[0]][spaceship_position[1]] = "."

while mission_status is None:
    command = input()

    move = directions[command]

    next_row = spaceship_position[0] + move[0]
    next_col = spaceship_position[1] + move[1]

    if not (0 <= next_row < n and 0 <= next_col < n):
        mission_status = "lost"
        break

    resources -= 5

    next_move = matrix[next_row][next_col]
    spaceship_position = (next_row, next_col)

    if next_move == "M":
        resources -= 5
        matrix[next_row][next_col] = '.'
    elif next_move == "R":
        resources = min(100, resources +10)
    elif next_move == "P":
        mission_status = "won"
        break

    if resources < 5:
        mission_status = "failed"

if mission_status == "won":
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
elif mission_status == "failed":
    matrix[spaceship_position[0]][spaceship_position[1]] = "S"
    print("Mission failed! The spaceship was stranded in space.")
elif mission_status == "lost":
    matrix[spaceship_position[0]][spaceship_position[1]] = "S"
    print("Mission failed! The spaceship was lost in space.")

for row in matrix:
        print(*row, sep=' ')