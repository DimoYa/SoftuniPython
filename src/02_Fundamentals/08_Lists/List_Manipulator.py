def exchange_command(list_param, parameters):
    index = int(parameters[0])
    if 0 <= index < len(list_param):
        elements_to_move = list_param[:index+1]
        del list_param[:index+1]
        list_param.extend(elements_to_move)
    else:
        print("Invalid index")
    return list_param


def max_command(list_param, parameters):
    even_or_odd = parameters[0]
    max_even_odd = None
    max_even_odd_index = -1

    for index, num in enumerate(list_param):
        if even_or_odd == "even" and num % 2 == 0:
            if max_even_odd is None or num >= max_even_odd:
                max_even_odd = num
                max_even_odd_index = index
        elif even_or_odd == "odd" and num % 2 != 0:
            if max_even_odd is None or num >= max_even_odd:
                max_even_odd = num
                max_even_odd_index = index

    if max_even_odd is None:
        print("No matches")
    else:
        print(max_even_odd_index)


def min_command(list_param, parameters):
    even_or_odd = parameters[0]
    min_even_odd = None
    min_even_odd_index = -1

    for index, num in enumerate(list_param):
        if even_or_odd == "even" and num % 2 == 0:
            if min_even_odd is None or num <= min_even_odd:
                min_even_odd = num
                min_even_odd_index = index
        elif even_or_odd == "odd" and num % 2 != 0:
            if min_even_odd is None or num <= min_even_odd:
                min_even_odd = num
                min_even_odd_index = index

    if min_even_odd is None:
        print("No matches")
    else:
        print(min_even_odd_index)


def first_command(list_param, parameters):
    count = int(parameters[0])
    even_or_odd = parameters[1]
    result = []

    if count > len(list_param):
        print("Invalid count")
        return None

    for num in list_param:
        if len(result) == count:
            break
        if even_or_odd == "even" and num % 2 == 0:
            result.append(num)
        elif even_or_odd == "odd" and num % 2 != 0:
            result.append(num)

    if len(result) == 0:
        print("[]")
    else:
        print(result)


def last_command(list_param, parameters):
    count = int(parameters[0])
    even_or_odd = parameters[1]
    result = []

    if count > len(list_param):
        print("Invalid count")
        return None

    for num in reversed(list_param):
        if len(result) == count:
            break
        if even_or_odd == "even" and num % 2 == 0:
            result.append(num)
        elif even_or_odd == "odd" and num % 2 != 0:
            result.append(num)

    result.reverse()
    if len(result) == 0:
        print("[]")
    else:
        print(result)


list_of_numbers = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break

    command_parts = command.split()
    command_name = command_parts[0]
    command_parameters = command_parts[1:]

    if command_name == "exchange":
        list_param = exchange_command(list_of_numbers, command_parameters)
    elif command_name == "max":
        max_command(list_of_numbers, command_parameters)
    elif command_name == "min":
        min_command(list_of_numbers, command_parameters)
    elif command_name == "first":
        first_command(list_of_numbers, command_parameters)
    elif command_name == "last":
        last_command(list_of_numbers, command_parameters)

print(list_of_numbers)