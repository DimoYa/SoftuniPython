n, m = [int(el) for el in input().split(", ")]

matrix = []
counter_terrorist_position = None
remaining_time = 16
bomb_defused = False
bomb_tried_to_defused = False

for row in range(n):
    line = [el for el in input()]
    matrix.append(line)
    if "C" in line:
        counter_terrorist_position = (row, line.index("C"))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


while remaining_time > 0:
    command = input()

    if command == "defuse":
        if matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] != "B":
            remaining_time -= 2
            continue
        else:
            if remaining_time >= 4:
                matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] = "D"
                remaining_time -= 4
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {remaining_time} second/s remaining.")
                bomb_defused = True
            else:
                matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] = "X"
                bomb_tried_to_defused = True
            break

    move = directions[command]
    next_row = counter_terrorist_position[0] + move[0]
    next_col = counter_terrorist_position[1] + move[1]

    remaining_time -= 1

    if not (0 <= next_row < n and 0 <= next_col < m):
        continue

    next_move = matrix[next_row][next_col]
    counter_terrorist_position = (next_row, next_col)

    if next_move == "T":
        matrix[next_row][next_col] = "*"
        print("Terrorists win!")
        break


if (remaining_time <= 0 and not bomb_defused) or bomb_tried_to_defused:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    if not bomb_tried_to_defused:
        remaining_time = 0
    else:
        remaining_time = 4 - remaining_time
    print(f"Time needed: {remaining_time} second/s.")

for row in matrix:
    print(*row, sep='')
