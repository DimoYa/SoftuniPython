def list_roman_emperors(*args, **kwargs):
    successful_dict = {}
    unsuccessful_dict = {}
    result = ""

    for name, status in args:
        if status:
            successful_dict[name] = 0
        else:
            unsuccessful_dict[name] = 0

    for name, rule in kwargs.items():
        if name in successful_dict:
            successful_dict[name] = rule
        if name in unsuccessful_dict:
            unsuccessful_dict[name] = rule

    result += f"Total number of emperors: {len(successful_dict) + len(unsuccessful_dict)}\n"

    if successful_dict:
        result += "Successful emperors:\n"
        for name, rule in sorted(successful_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])):
            result += f"****{name}: {rule}\n"

    if unsuccessful_dict:
        result += "Unsuccessful emperors:\n"
        for name, rule in sorted(unsuccessful_dict.items(), key=lambda kvp: (kvp[1], kvp[0])):
            result += f"****{name}: {rule}\n"

    return result


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))