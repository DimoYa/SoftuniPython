def list_roman_emperors(*args, **kwargs):
    successful = {}
    unsuccessful = {}

    for name, status in args:
        if status:
            successful[name] = kwargs.get(name, 0)
        else:
            unsuccessful[name] = kwargs.get(name, 0)

    result = f"Total number of emperors: {len(successful) + len(unsuccessful)}\n"

    if successful:
        result += "Successful emperors:\n"
        for name, years in sorted(successful.items(), key=lambda x: (-x[1], x[0])):
            result += f"****{name}: {years}\n"

    if unsuccessful:
        result += "Unsuccessful emperors:\n"
        for name, years in sorted(unsuccessful.items(), key=lambda x: (x[1], x[0])):
            result += f"****{name}: {years}\n"

    return result.strip()


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print("-------------------------------------------------------------------------------")
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print("-------------------------------------------------------------------------------")
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))