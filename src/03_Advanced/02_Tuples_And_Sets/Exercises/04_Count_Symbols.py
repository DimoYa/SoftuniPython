text = input()
counter = {}

for index in range(len(text)):
    current_char = text[index]

    if current_char not in counter:
        counter[current_char] = 0
    counter[current_char] += 1

for key, value in sorted(counter.items()):
    print(f"{key}: {value} time/s")
