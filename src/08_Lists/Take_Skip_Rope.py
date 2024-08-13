def take_skip(arr, take_n, skip_n, final_string):
    final_string += "".join(arr[:take_n])
    arr = arr[take_n:]
    arr = arr[skip_n:]

    return arr, final_string


line = input()
final_string = ""

digit = [int(dig) for dig in line if dig.isdigit()]
non_digit = [dig for dig in line if not dig.isdigit()]
take_list = [num for i, num in enumerate(digit) if i % 2 == 0]
skip_list = [num for i, num in enumerate(digit) if not i % 2 == 0]

for i in range(len(take_list)):
    current_take = take_list[i]
    current_skip = skip_list[i]

    non_digit, final_string = take_skip(non_digit, current_take, current_skip, final_string)

print(final_string)