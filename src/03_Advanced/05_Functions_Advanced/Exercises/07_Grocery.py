def grocery_store(**kwargs):

    items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return "\n".join(f"{i[0]}: {i[1]}" for i in items)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
