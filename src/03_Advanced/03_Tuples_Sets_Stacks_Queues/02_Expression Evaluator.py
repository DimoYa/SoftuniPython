import math
from collections import deque


def is_integer(s):
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()


expression = input().split()

numbers_as_stack = deque()
current_result = 0

for sym in expression:
    if is_integer(sym):
        numbers_as_stack.append(int(sym))
    else:
        operation = sym
        current_result = numbers_as_stack.popleft()
        while numbers_as_stack:
            if sym == "+":
                current_result += numbers_as_stack.popleft()
            elif sym == "-":
                current_result -= numbers_as_stack.popleft()
            elif sym == "*":
                current_result *= numbers_as_stack.popleft()
            elif sym == "/":
                current_result /= numbers_as_stack.popleft()
                current_result = math.floor(current_result)
        numbers_as_stack.append(current_result)

print(current_result)
