def even_odd(*arg):
    result = []

    even_or_odd = arg[-1]
    numbers = arg[:-1]

    if even_or_odd == "even":
        result.extend([el for el in numbers if el % 2 == 0])
    else:
        result.extend([el for el in numbers if el % 2 != 0])

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
