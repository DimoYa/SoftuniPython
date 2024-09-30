input_str = input().split("|")

flattened_list = []

for sub_list in reversed(input_str):
    numbers = sub_list.split()
    flattened_list.extend(numbers)

print(" ".join(flattened_list))
