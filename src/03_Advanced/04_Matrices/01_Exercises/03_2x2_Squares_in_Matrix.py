rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for row in range(rows)]

square_matrices = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        left = matrix[row][col]
        right = matrix[row][col + 1]
        below = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]

        if left == right == below == diagonal:
            square_matrices += 1

print(square_matrices)