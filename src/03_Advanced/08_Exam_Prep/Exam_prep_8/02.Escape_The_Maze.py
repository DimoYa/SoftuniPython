n = int(input())
matrix = []
traveler_position = None
traveler_health = 100
mission_status = None  # "won", "failed"

for row in range(n):
    line = input()
    matrix.append([el for el in line])
    if "P" in line:
        traveler_position = row, line.index("P")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[traveler_position[0]][traveler_position[1]] = "-"

while traveler_health > 0:
    command = input()

    move = directions[command]

    next_row = traveler_position[0] + move[0]
    next_col = traveler_position[1] + move[1]

    if not (0 <= next_row < n and 0 <= next_col < n):
        continue

    next_move = matrix[next_row][next_col]
    traveler_position = (next_row, next_col)

    if next_move == "M":
        traveler_health -= 40
        if traveler_health <= 0:
            traveler_health = 0
            mission_status = "failed"
            break
        matrix[next_row][next_col] = '-'
    elif next_move == "H":
        traveler_health = min(100, traveler_health +15)
        matrix[next_row][next_col] = '-'
    elif next_move == "X":
        mission_status = "won"
        break

matrix[traveler_position[0]][traveler_position[1]] = "P"
if traveler_health == 0 or mission_status == "failed":
    print("Player is dead. Maze over!")
elif traveler_health > 0 and mission_status == "won":
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {traveler_health} units")

for row in matrix:
        print(*row, sep='')