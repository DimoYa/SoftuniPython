def merge_command(arr, parameters):
    start_index = int(parameters[0])
    end_index = int(parameters[1])

    merged_items = ""

    start_index = max(0, start_index)
    end_index = min(len(arr), end_index + 1)

    for i in range(start_index, end_index):
        merged_items += arr[i]

    del arr[start_index:end_index]

    arr.insert(start_index, merged_items)
    return arr


def divide_command(arr, parameters):
    index = int(parameters[0])
    num_parts = int(parameters[1])

    s = arr[index]

    part_length = len(s) // num_parts
    remainder = len(s) % num_parts

    parts = []
    start = 0
    for i in range(num_parts):
        end = start + part_length + (1 if i < remainder else 0)
        parts.append(s[start:end])
        start = end

    arr.pop(index)
    arr[index:index] = parts

    return arr


input_data = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    command_part = command.split()
    command_name = command_part[0]
    command_parameters = command_part[1:]

    if command_name == "merge":
        input_data = merge_command(input_data, command_parameters)
    else:
        input_data = divide_command(input_data, command_parameters)

print(' '.join(input_data))
