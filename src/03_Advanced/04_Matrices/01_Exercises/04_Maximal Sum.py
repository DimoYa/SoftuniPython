rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for row in range(rows)]

maximum_sum = float('-inf')
maximum_sub_start = 0
maximum_sub_end = 0


for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix_sum = 0
        current_start = row
        current_end = col
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                current_el = int(matrix[i][j])
                current_matrix_sum += current_el
        if current_matrix_sum > maximum_sum:
            maximum_sum = current_matrix_sum
            maximum_sub_start = current_start
            maximum_sub_end = current_end

print(f"Sum = {maximum_sum}")
for row in range(maximum_sub_start, maximum_sub_start + 3):
    for col in range(maximum_sub_end, maximum_sub_end + 3):
        print(matrix[row][col], end=' ')
    print()
