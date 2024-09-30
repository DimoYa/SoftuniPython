n = int(input())

matrix = []
bunny_position = []
max_collected_eggs = float("-inf")
max_collected_path = []
maximum_direction = ""

for row in range(n):
    matrix.append([x for x in input().split()])
    for col in range(n):
        if matrix[row][col] == "B":
            bunny_position.extend([row, col])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for direction, move in directions.items():

    collected_eggs = 0
    collected_coordinates = []
    current_bunny_row = bunny_position[0]
    current_bunny_col = bunny_position[1]

    while True:
        next_row = current_bunny_row + (move[0])
        next_col = current_bunny_col + (move[1])

        if not (0 <= next_row < n and 0 <= next_col < n):
            break

        current_position = matrix[next_row][next_col]

        if current_position == "X":
            break

        collected_eggs += int(current_position)
        collected_coordinates.append([next_row, next_col])

        current_bunny_row = next_row
        current_bunny_col = next_col

    if collected_eggs > max_collected_eggs and collected_coordinates:
        max_collected_eggs = collected_eggs
        max_collected_path = collected_coordinates
        maximum_direction = direction

print(maximum_direction)
print(*max_collected_path, sep='\n')
print(max_collected_eggs)
