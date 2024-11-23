def genrange(start, end):
    for i in range(start - 1, end):
        yield i+1


print(list(genrange(1, 10)))
