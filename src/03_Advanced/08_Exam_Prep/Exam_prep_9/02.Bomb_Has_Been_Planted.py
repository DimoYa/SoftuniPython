rows, cols = [int(el) for el in input().split(", ")]

matrix = []
start_position = None
ct_position = None
time_left = 16
bomb_defused = False
mission_status = None  # 'won', 'killed', 'failed'

# Read map and locate 'C'
for r in range(rows):
    line = list(input())
    matrix.append(line)
    if 'C' in line:
        start_position = (r, line.index('C'))
        ct_position = start_position

# Directions map
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Remove the 'C' for movement (restore at end)
matrix[ct_position[0]][ct_position[1]] = '*'

while time_left > 0:
    command = input()

    if command == "defuse":
        current_cell = matrix[ct_position[0]][ct_position[1]]
        if current_cell == 'B':
            time_left -= 4
            if time_left > 0:
                matrix[ct_position[0]][ct_position[1]] = 'D'
                mission_status = 'won'
            else:
                matrix[ct_position[0]][ct_position[1]] = 'X'
                mission_status = 'failed'
            break
        else:
            time_left -= 2
            continue

    elif command in directions:
        dr, dc = directions[command]
        next_r = ct_position[0] + dr
        next_c = ct_position[1] + dc

        time_left -= 1

        # Check map boundaries
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            continue  # time still deducted, but position stays

        next_cell = matrix[next_r][next_c]

        if next_cell == 'T':
            matrix[next_r][next_c] = '*'
            mission_status = 'killed'
            break
        else:
            ct_position = (next_r, next_c)

    else:
        continue  # Invalid command ignored

# Determine outcome and print messages
if mission_status == 'won':
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time_left} second/s remaining.")
elif mission_status == 'killed':
    print("Terrorists win!")
elif mission_status == 'failed' or time_left <= 0:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {max(0, time_left - 4)} second/s.")

# Restore original CT position to the map
matrix[start_position[0]][start_position[1]] = 'C'

# Print final map
for row in matrix:
    print("".join(row))
