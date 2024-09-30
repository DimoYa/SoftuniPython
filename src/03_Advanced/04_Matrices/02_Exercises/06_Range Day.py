def directions(direction_var, steps_count):
    moves = {
        'up': (-steps_count, 0),
        'down': (steps_count, 0),
        'left': (0, -steps_count),
        'right': (0, steps_count)
    }
    return moves[direction_var]


def shoot(matrix, player_position, direction, dimensions):
    counter = 1
    while True:
        next_row, next_col = directions(direction, counter)
        next_row += player_position[0]
        next_col += player_position[1]

        if not (0 <= next_row < dimensions and 0 <= next_col < dimensions):
            break  # Stop if out of bounds

        if matrix[next_row][next_col] == "x":  # Target found
            matrix[next_row][next_col] = "."  # Mark as shot
            return True, [next_row, next_col]  # Return hit target position

        counter += 1
    return False, []  # No target hit


def move_player(matrix, player_position, direction, steps, dimensions):
    next_row, next_col = directions(direction, steps)
    next_row += player_position[0]
    next_col += player_position[1]

    # Check if movement is within bounds and valid
    if 0 <= next_row < dimensions and 0 <= next_col < dimensions:
        if matrix[next_row][next_col] == ".":
            # Move player
            matrix[next_row][next_col] = "A"
            matrix[player_position[0]][player_position[1]] = "."
            return [next_row, next_col]

    return player_position  # Return current position if move is invalid


# Initialize the game
dimensions = 5
matrix = []
player_position = []
targets_to_shoot = 0

# Read the matrix
for row in range(dimensions):
    matrix.append(input().split())
    for col in range(dimensions):
        if matrix[row][col] == "A":
            player_position = [row, col]
        elif matrix[row][col] == "x":
            targets_to_shoot += 1

command_numbers = int(input())
shoot_targets = []

# Process commands
for _ in range(command_numbers):
    command = input().split()

    if command[0] == "shoot":
        direction = command[1]
        hit, target_position = shoot(matrix, player_position, direction, dimensions)
        if hit:
            shoot_targets.append(target_position)
            targets_to_shoot -= 1  # Decrease target count

        if targets_to_shoot == 0:  # If all targets are shot
            print(f"Training completed! All {len(shoot_targets)} targets hit.")
            break

    elif command[0] == "move":
        direction, steps = command[1:]
        steps = int(steps)
        player_position = move_player(matrix, player_position, direction, steps, dimensions)

# Check if all targets are hit after processing commands
if targets_to_shoot > 0:
    print(f"Training not completed! {targets_to_shoot} targets left.")

# Print all hit targets
for target in shoot_targets:
    print(target)
