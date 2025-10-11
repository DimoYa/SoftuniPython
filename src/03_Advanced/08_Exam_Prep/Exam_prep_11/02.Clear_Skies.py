n = int(input())

matrix = []
jet_fighter_position = None
mission_status = None  # "won", "failed"
armour_amount = 300
shoot_enemies = 0

for row in range(n):
    line = input()
    matrix.append([el for el in line])
    if "J" in line:
        jet_fighter_position = row, line.index("J")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[jet_fighter_position[0]][jet_fighter_position[1]] = "-"

while armour_amount > 0 and shoot_enemies < 4:
    command = input()

    move = directions[command]

    next_row = jet_fighter_position[0] + move[0]
    next_col = jet_fighter_position[1] + move[1]

    next_move = matrix[next_row][next_col]
    jet_fighter_position = (next_row, next_col)

    if next_move == "E":
        shoot_enemies += 1
        armour_amount -= 100

    elif next_move == "R":
        armour_amount = 300

    matrix[next_row][next_col] = '-'

matrix[jet_fighter_position[0]][jet_fighter_position[1]] = "J"

if shoot_enemies == 4:
    print("Mission accomplished, you neutralized the aerial threat!")

if armour_amount == 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_fighter_position[0]}, {jet_fighter_position[1]}]!")

for row in matrix:
        print(*row, sep='')