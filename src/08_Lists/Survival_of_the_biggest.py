def get_smallest_n_numbers(arr, count):
    sorted_arr = sorted(arr)
    return  sorted_arr[:count]


def remove_items_from_array(arr, arr_to_remove):
    result = []
    for item in arr:
        if item not in arr_to_remove:
            result.append(item)
    return result


numbers = input().split()
n = int(input())

number_list = []

for num in numbers:
    number_list.append(int(num))

smallest_n_numbers = get_smallest_n_numbers(number_list, n)
final_arr = remove_items_from_array(number_list, smallest_n_numbers)
print(', '.join(map(str, final_arr)))
