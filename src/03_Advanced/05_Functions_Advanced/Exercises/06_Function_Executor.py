def func_executor(*args):
    result = []

    for el in args:
        function = el[0]
        arguments = el[1]
        result.append(f"{function.__name__} - {function(*arguments)}")
    return "\n".join(result)


# output
def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
