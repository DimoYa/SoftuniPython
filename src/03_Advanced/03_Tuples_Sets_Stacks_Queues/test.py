row_size, col_size = [int(el) for el in input().split(", ")]

matrix = []
max_sum = -10000
max_sub_matrix = []


for row in range(row_size):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

for row in range(row_size - 1):
    for col in range(len(matrix[row]) - 1):
        left = matrix[row][col]
        right = matrix[row][col + 1]
        down = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]
        sum_sub_matrix = left + right + down + diagonal
        if sum_sub_matrix > max_sum:
            max_sum = sum_sub_matrix
            max_sub_matrix = [
                [left, right],
                [down, diagonal]
            ]

for row in max_sub_matrix:
    print(" ".join(map(str, row)))
print(max_sum)