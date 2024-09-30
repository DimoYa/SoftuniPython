n = int(input())

matrix = []
alice_position = []
collected_bags = 0
is_collected = False


for row in range(n):
    matrix.append([x for x in input().split()])
    for col in range(n):
        if matrix[row][col] == "A":
            alice_position = [row, col]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[alice_position[0]][alice_position[1]] = "*"

while True:

    command = input()
    move = directions[command]

    next_row = alice_position[0] + (move[0])
    next_col = alice_position[1] + (move[1])

    if not (0 <= next_row < n and 0 <= next_col < n):
        break

    if matrix[next_row][next_col] == "R":
        matrix[next_row][next_col] = "*"
        break

    if matrix[next_row][next_col].isdigit():
        collected_bags += int(matrix[next_row][next_col])

    alice_position = [next_row, next_col]
    matrix[next_row][next_col] = "*"

    if collected_bags >= 10:
        is_collected = True
        break

if is_collected:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)