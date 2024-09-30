n = int(input())

matrix = [[int(row) for row in input().split(", ")] for row in range(n)]

primary_diagonals = []
secondary_diagonals = []


for i in range(n):
    primary_diagonals.append(matrix[i][i])

for i in range(n-1, -1, -1):
    secondary_diagonals.append(matrix[n-i-1][i])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonals])}. Sum: {sum(primary_diagonals)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonals])}. Sum: {sum(secondary_diagonals)}")
