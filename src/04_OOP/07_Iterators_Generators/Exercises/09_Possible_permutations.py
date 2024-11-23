from itertools import permutations


def possible_permutations(data):
    perms = permutations(data)
    for perm in perms:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]