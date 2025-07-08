from collections import deque

# Input parsing
strengths_stack = [int(el) for el in input().split()]
accuracies_queue = deque([int(el) for el in input().split()])
scored_goals = 0

# Process while both lists have elements
while strengths_stack and accuracies_queue:
    strength = strengths_stack[-1]
    accuracy = accuracies_queue[0]
    total = strength + accuracy

    if total == 100:
        strengths_stack.pop()
        accuracies_queue.popleft()
        scored_goals += 1
    elif total < 100:
        if strength < accuracy:
            strengths_stack.pop()
        elif accuracy < strength:
            accuracies_queue.popleft()
        else:
            # Equal: remove both and push back the sum
            strengths_stack.pop()
            accuracies_queue.popleft()
            strengths_stack.append(total)
    else:  # total > 100
        strengths_stack[-1] -= 10
        accuracies_queue.append(accuracies_queue.popleft())

# Output result
if scored_goals == 0:
    print("Paul failed to score a single goal.")
else:
    if scored_goals == 3:
        print("Paul scored a hat-trick!")
    elif scored_goals > 3:
        print("Paul performed remarkably well!")
    else:
        print("Paul failed to make a hat-trick.")
    print(f"Goals scored: {scored_goals}")

# Print remaining values, if any
if strengths_stack:
    print(f"Strength values left: {', '.join(map(str, strengths_stack))}")
if accuracies_queue:
    print(f"Accuracy values left: {', '.join(map(str, accuracies_queue))}")
