source_string = input()
target_string = input()

index = 0

for char in range(len(source_string)):
    current_char = target_string[index]
    if current_char != source_string[index]:
        source_string = source_string[:index] + current_char + source_string[index + 1:]
        print(source_string)
    index += 1