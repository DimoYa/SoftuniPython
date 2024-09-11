parentheses = input()
stack = []
opening_brackets = ["(", "[", "{"]
closing_brackets = [")", "]", "}"]
is_equal = True

for index in range(len(parentheses)):
    if parentheses[index] in opening_brackets:
        stack.append(parentheses[index])
    elif parentheses[index] in closing_brackets:
        bracket_index = closing_brackets.index(parentheses[index])
        if opening_brackets[bracket_index] in stack:
            stack.pop()
        else:
            is_equal = False
if is_equal:
    print("YES")
else:
    print("NO")
