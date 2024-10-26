n = int(input())

matrix = []
gambler_position = None
initial_amount = 100
jackpot_won = False
lost_game = False

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
        lost_game = True
        break

    next_move = matrix[next_row][next_col]
    gambler_position = (next_row, next_col)

    if next_move == "W":
        initial_amount += 100
    elif next_move == "P":
        initial_amount -= 200
    elif next_move == "J":
        jackpot_won = True
        initial_amount += 100000
        break

    if initial_amount <= 0:
        lost_game = True
        break

    matrix[next_row][next_col] = "-"

matrix[gambler_position[0]][gambler_position[1]] = "G"

if jackpot_won and not lost_game:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {initial_amount}$")
if not jackpot_won and initial_amount > 0:
    print(f"End of the game. Total amount: {initial_amount}$")
if lost_game and initial_amount <= 0:
    print("Game over! You lost everything!")

if initial_amount > 0:
    for row in matrix:
        print(*row, sep='')
