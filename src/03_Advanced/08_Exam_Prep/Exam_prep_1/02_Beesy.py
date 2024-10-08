n = int(input())

matrix = []
bee_position = []
initial_energy = 15
units_of_nectar_goals = 30
collected_nectar = 0
is_restored = False
hive_reached = False

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "B":
            bee_position.extend([row, col])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()

    move = directions[command]

    # Calculate next position
    next_row = bee_position[0] + move[0]
    next_col = bee_position[1] + move[1]

    # Wrap around if out of bounds
    if next_row < 0:
        next_row = n - 1
    elif next_row >= n:
        next_row = 0

    if next_col < 0:
        next_col = n - 1
    elif next_col >= n:
        next_col = 0

    matrix[bee_position[0]][bee_position[1]] = "-"

    if matrix[next_row][next_col].isdigit():
        collected_nectar += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = "-"

    # Update bee's position
    bee_position = [next_row, next_col]

    initial_energy -= 1

    if matrix[next_row][next_col] == "H":
        hive_reached = True
        break

    if initial_energy == 0:
        if collected_nectar >= units_of_nectar_goals and not is_restored:
            # Restore energy and reduce nectar to 30
            initial_energy += (collected_nectar - units_of_nectar_goals)
            is_restored = True
            collected_nectar = 30
        else:
            break

matrix[bee_position[0]][bee_position[1]] = "B"

if hive_reached and collected_nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")

elif hive_reached and collected_nectar < units_of_nectar_goals:
    print(f"Beesy did not manage to collect enough nectar.")

elif not hive_reached and initial_energy == 0:
    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print(*row, sep='')
