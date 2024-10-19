n = int(input())
matrix = []
player_position = None
collected_amount = 0
required_quaota = 20
got_into_whirlpool = False

for row in range(n):
    matrix.append([el for el in input()])
    for col in range(n):
        if matrix[row][col] == "S":
            player_position = (row, col)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[player_position[0]][player_position[1]] = "-"

while True:
    command = input()

    if command == "collect the nets":
        break

    move = directions[command]

    next_row = player_position[0] + move[0]
    next_col = player_position[1] + move[1]

    # Wrap around if out of bounds
    if next_row < 0:
        next_row = n - 1
    elif next_row >= n:
        next_row = 0

    if next_col < 0:
        next_col = n - 1
    elif next_col >= n:
        next_col = 0

    next_move = matrix[next_row][next_col]
    player_position = (next_row, next_col)

    if next_move.isdigit():
        collected_amount += int(next_move)
        matrix[next_row][next_col] = "-"

    if next_move == "W":
        collected_amount = 0
        print(f"You fell into a whirlpool!"
              f" The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{player_position[0]},{player_position[1]}]")
        got_into_whirlpool = True
        break
matrix[player_position[0]][player_position[1]] = "S"
if not got_into_whirlpool:
    if collected_amount >= required_quaota:
        print("Success! You managed to reach the quota!")
    else:
        print("You didn't catch enough fish and didn't reach the quota!"
              f" You need {required_quaota - collected_amount} tons of fish more.")

    if collected_amount:
        print(f"Amount of fish caught: {collected_amount} tons.")

    if not got_into_whirlpool:
        for row in matrix:
            print(*row, sep="")
