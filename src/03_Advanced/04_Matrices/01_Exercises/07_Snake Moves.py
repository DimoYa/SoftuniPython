# Get the dimensions of the matrix
rows, cols = [int(el) for el in input().split()]
word = input()

# Ensure the word is long enough by repeating it if necessary
full_word = (word * ((rows * cols) // len(word) + 1))[:rows * cols]

# Prepare the matrix
matrix = []

for row in range(rows):
    start_index = row * cols
    current_row = full_word[start_index:start_index + cols]

    # For odd rows, reverse the current_row
    if row % 2 == 1:
        current_row = current_row[::-1]

    matrix.append(current_row)

# Print the resulting matrix
for row in matrix:
    print(row)
