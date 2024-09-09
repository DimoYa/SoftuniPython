expression = input()

list_as_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        list_as_stack.append(index)
    elif expression[index] == ")":
        stat_index = list_as_stack.pop()
        end_index = index + 1
        print(expression[stat_index:end_index])