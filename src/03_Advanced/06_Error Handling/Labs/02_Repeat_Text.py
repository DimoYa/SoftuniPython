text = input()
try:
    time = int(input())
    print(text * time)
except ValueError:
    print("Variable times must be an integer")



