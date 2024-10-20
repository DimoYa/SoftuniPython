from collections import deque

strength = [int(el) for el in input().split()]
accuracy = deque([int(el) for el in input().split()])
goal_required = 100
scored_goals = 0

while strength and accuracy:

    current_strength = strength[-1]
    current_accuracy = accuracy[0]

    current_sum = current_strength + current_accuracy

    if current_sum == goal_required:
        strength.pop()
        accuracy.popleft()
        scored_goals += 1
    elif current_sum < goal_required:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            strength.pop()
            accuracy.popleft()
            strength.append(current_sum)
    else:
        accuracy.popleft()
        strength[-1] -= 10
        accuracy.append(current_accuracy)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
if scored_goals == 0:
    print("Paul failed to score a single goal.")
if scored_goals > 3:
    print("Paul performed remarkably well!")
if 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")
if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")
if strength:
    print(f"Strength values left: {', '.join(map(str, strength))}")
if accuracy:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")
