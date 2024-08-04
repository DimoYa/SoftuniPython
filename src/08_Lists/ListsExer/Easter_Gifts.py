def out_of_stock(original_arr, parameter):
    to_be_replaced = parameter[0]
    for i in range(len(original_arr)):
        if original_arr[i] == to_be_replaced:
            original_arr[i] = "None"
    return original_arr


def required(original_arr, parameter):
    gift = parameter[0]
    index = int(parameter[1])
    if 0 <= index < len(original_arr):
        original_arr[index] = gift
    return original_arr


def just_in_case(original_arr, parameter):
    original_arr[-1] = parameter[0]
    return original_arr


names_of_gifts = input().split()

while True:
    commands = input()

    if commands == "No Money":
        break

    command_part = commands.split()
    command_name = command_part[0]
    command_parameters = command_part[1:]

    if command_name == "OutOfStock":
        names_of_gifts = out_of_stock(names_of_gifts, command_parameters)
    elif command_name == "Required":
        names_of_gifts = required(names_of_gifts, command_parameters)
    else:
        names_of_gifts = just_in_case(names_of_gifts, command_parameters)

filtered_list = []
for item in names_of_gifts:
    if item != "None":
        filtered_list.append(item)

print(' '.join(filtered_list))