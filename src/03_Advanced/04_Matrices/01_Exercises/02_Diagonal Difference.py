def formatted_diagonal(array):
    return [f"({el})" if el < 0 else str(el) for el in array]


n = int(input())

matrix = [[int(row) for row in input().split()] for row in range(n)]

primary_diagonals = []
secondary_diagonals = []


for i in range(n):
    primary_diagonals.append(matrix[i][i])

for i in range(n-1, -1, -1):
    secondary_diagonals.append(matrix[n-i-1][i])


# print(f"Primary diagonal: sum = {' + '.join(formatted_diagonal(primary_diagonals))} = {sum(primary_diagonals)}")
# print(f"Secondary diagonal: sum = {' + '.join(formatted_diagonal(secondary_diagonals))} = {sum(secondary_diagonals)}")
# print(f"Difference: |{sum(primary_diagonals)} - {sum(secondary_diagonals)}|"
#       f" = {abs(sum(primary_diagonals) - sum(secondary_diagonals))}")
print(abs(sum(primary_diagonals) - sum(secondary_diagonals)))
