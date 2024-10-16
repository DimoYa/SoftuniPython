field_size = int(input())

matrix = []
player_position = None
collected_stars = 2

for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        if matrix[row][col] == "P":
            player_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while 0 < collected_stars < 10:

    command = input()

    move = directions[command]

    # Calculate next position
    next_row = player_position[0] + move[0]
    next_col = player_position[1] + move[1]

    if not (0 <= next_row < field_size and 0 <= next_col < field_size):
        next_row, next_col = [0, 0]  # Teleport to starting position

    next_field = matrix[next_row][next_col]

    if next_field == "*":
        collected_stars += 1
        matrix[next_row][next_col] = "."
        matrix[player_position[0]][player_position[1]] = "."
        player_position = next_row, next_col
        matrix[player_position[0]][player_position[1]] = "P"
    elif next_field == "#":
        collected_stars -= 1
    else:
        matrix[player_position[0]][player_position[1]] = "."
        player_position = next_row, next_col
        matrix[player_position[0]][player_position[1]] = "P"

if collected_stars == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")
for row in matrix:
    print(*row, sep=" ")
