from collections import deque

worm_size_stack = [int(el) for el in input().split()]
hole_size_queue = deque([int(el) for el in input().split()])
initial_worm_count = len(worm_size_stack)
matchesCount = 0

while worm_size_stack and hole_size_queue:
    current_worm = worm_size_stack[-1]
    current_size = hole_size_queue[0]

    if current_worm == current_size:
        worm_size_stack.pop()
        hole_size_queue.popleft()
        matchesCount +=1
    else:
        hole_size_queue.popleft()
        worm_size_stack[-1] -= 3
        if worm_size_stack[-1] <= 0:
            worm_size_stack.pop()

result = ""

if matchesCount:
    result += f"Matches: {matchesCount}\n"
else:
    result += "There are no matches.\n"

if not worm_size_stack and initial_worm_count == matchesCount:
    result += "Every worm found a suitable hole!\n"

if not worm_size_stack and initial_worm_count != matchesCount:
    result += "Worms left: none\n"
if worm_size_stack and initial_worm_count != matchesCount:
    result += f"Worms left: {', '.join(str(w) for w in worm_size_stack)}\n"

if not hole_size_queue:
    result += "Holes left: none\n"
else:
    result += f"Holes left: {', '.join(str(h) for h in hole_size_queue)}"

print(result)