m = int(input())
n = int(input())

matrix = []
initial_nice_kids = 0
santa_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa_position = [row, col]
        elif matrix[row][col] == "V":
            initial_nice_kids += 1


nice_kids_to_deliver = initial_nice_kids

while m > 0:

    command = input()
    if command == "Christmas morning":
        break
    movement = directions[command]

    next_row = santa_position[0] + (movement[0])
    next_col = santa_position[1] + (movement[1])

    if not (0 <= next_row < n and 0 <= next_col < n):
        break

    symbol = matrix[next_row][next_col]

    if symbol == "C":
        matrix[santa_position[0]][santa_position[1]] = "-"
        matrix[next_row][next_col] = "S"
        santa_position = next_row, next_col

        for way, pos in directions.items():

            next_row = santa_position[0] + (pos[0])
            next_col = santa_position[1] + (pos[1])

            if not (0 <= next_row < n and 0 <= next_col < n):
                break

            symbol = matrix[next_row][next_col]

            if symbol == "V":
                m -= 1
                nice_kids_to_deliver -= 1
            elif symbol == "X":
                m -= 1

            matrix[next_row][next_col] = "-"
    else:
        if symbol == "V":
            m -= 1
            nice_kids_to_deliver -= 1

        matrix[santa_position[0]][santa_position[1]] = "-"
        matrix[next_row][next_col] = "S"
        santa_position = next_row, next_col

if m == 0 and nice_kids_to_deliver:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)
if not nice_kids_to_deliver:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids_to_deliver} nice kid/s.")
