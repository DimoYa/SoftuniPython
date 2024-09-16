first_set = set([int(num) for num in input().split()])
second_set = set([int(num) for num in input().split()])
n = int(input())


def add_first_command(params):
    first_set.update(map(int, params))  # Convert params to integers before adding


def add_second_command(params):
    second_set.update(map(int, params))  # Convert params to integers before adding


def remove_first_command(params):
    first_set.difference_update(map(int, params))  # Remove integers from first_set


def remove_second_command(params):
    second_set.difference_update(map(int, params))  # Remove integers from second_set


def check_subset_command():
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        print("True")
    else:
        print("False")


for _ in range(n):
    line = input().split()
    command = line[0]
    target = line[1]
    num_params = line[2:]

    if command == "Add" and target == "First":
        add_first_command(num_params)
    elif command == "Add" and target == "Second":
        add_second_command(num_params)
    elif command == "Remove" and target == "First":
        remove_first_command(num_params)
    elif command == "Remove" and target == "Second":
        remove_second_command(num_params)
    elif command == "Check" and target == "Subset":
        check_subset_command()

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
