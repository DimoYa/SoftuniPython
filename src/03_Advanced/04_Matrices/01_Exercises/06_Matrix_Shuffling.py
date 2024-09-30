rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(el) for el in command[1:]]

    if not (0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row)
