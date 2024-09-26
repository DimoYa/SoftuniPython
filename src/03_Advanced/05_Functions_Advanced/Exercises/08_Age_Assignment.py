def age_assignment(*args, **kwargs):
    result = {}
    for item in args:
        result[item] = kwargs[item[0]]

    return "\n".join(f"{name} is {age} years old." for name, age in sorted(result.items()))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
