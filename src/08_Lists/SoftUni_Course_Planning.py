def get_item_index(array, item):
    try:
        return array.index(item)
    except ValueError:
        return -1


def add_command(arr, args):
    lesson_title = args[0]

    if lesson_title not in arr:
        arr.append(lesson_title)

    return arr


def insert_command(arr, args):
    lesson_title = args[0]
    index = int(args[1])

    if lesson_title not in arr:
        arr.insert(index, lesson_title)

    return arr


def remove_command(arr, args):
    lesson_title = args[0]

    if lesson_title in arr:
        arr.remove(lesson_title)

    return arr


def swap_command(arr, args):
    first_item = args[0]
    second_item = args[1]

    if first_item in arr and second_item in arr:
        first_item_index = arr.index(first_item)
        second_item_index = arr.index(second_item)

        arr.remove(first_item)
        arr.insert(first_item_index, second_item)

        arr.remove(second_item)
        arr.insert(second_item_index, first_item)

    return arr


def exercise_command(arr, args):
    lesson_title = args[0]
    item_index = int(args.index(lesson_title))

    if lesson_title in arr:
        item_index = get_item_index(arr, lesson_title)
        if item_index + 1 < len(arr) and arr[item_index + 1] != f"{lesson_title}-Exercise":
            arr.insert(item_index + 1, f"{lesson_title}-Exercise")

    return []


lessons = input().split(", ")

while True:

    command = input()

    if command == "course start":
        break

    command_parts = command.split(":")
    command_name = command_parts[0]
    command_args = command_parts[1:]

    if command_name == "Add":
        lessons = add_command(lessons, command_args)
    elif command_name == "Insert":
        lessons = insert_command(lessons, command_args)
    elif command_name == "Remove":
        lessons = remove_command(lessons, command_args)
    elif command_name == "Swap":
        lessons = swap_command(lessons, command_args)
    else:
        lessons = exercise_command(lessons, command_args)

for i, lesson in enumerate(lessons):
    print(f"{i + 1}.{lesson}")
