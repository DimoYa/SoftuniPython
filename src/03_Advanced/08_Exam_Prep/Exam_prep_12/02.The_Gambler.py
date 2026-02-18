n = int(input())

matrix = []
gambler_position = None
game_status = None  # "won", "failed"
game_amount = 100

for row in range(n):
    line = input()
    matrix.append([el for el in line])
    if "G" in line:
        gambler_position = row, line.index("G")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[gambler_position[0]][gambler_position[1]] = "-"

while True:
    command = input()

    if command == "end":
        break

    move = directions[command]

    next_row = gambler_position[0] + move[0]
    next_col = gambler_position[1] + move[1]

    if not (0 <= next_row < n and 0 <= next_col < n):
        game_status = "failed"
        break

    next_move = matrix[next_row][next_col]
    gambler_position = (next_row, next_col)

    if next_move == "W":
        game_amount += 100

    elif next_move == "P":
        game_amount -= 200

    elif next_move == "J":
        game_amount += 100000
        game_status = "won"
        break

    if game_amount <= 0:
        game_status = "failed"
        break

    matrix[next_row][next_col] = '-'

matrix[gambler_position[0]][gambler_position[1]] = "G"

if game_status == "won":
    print(f"You win the Jackpot! End of the game. Total amount: {game_amount}$")
elif game_status == "failed":
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {game_amount}$")

if game_status != "failed":
    for row in matrix:
        print(*row, sep='')