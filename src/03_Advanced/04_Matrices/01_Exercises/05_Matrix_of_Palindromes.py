rows, cols = [int(el) for el in input().split()]

counter = 0
for row in range(rows):
    for col in range(cols):
        print(f"{chr(97+row)}{chr(97+col+counter)}{chr(97+row)}", end=" ")
    counter += 1
    print()
