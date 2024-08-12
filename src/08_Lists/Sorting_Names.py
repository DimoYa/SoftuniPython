names = input().split(", ")
names.sort(key= lambda x: (-len(x), x))
print(names)
