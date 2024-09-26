def concatenate(*args, **kwargs):
    result = "".join(args)
    for k, v in kwargs.items():
        result = result.replace(k, v)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

