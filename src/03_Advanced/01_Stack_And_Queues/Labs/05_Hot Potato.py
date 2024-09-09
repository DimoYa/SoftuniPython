from collections import deque

kids = deque(input().split())
hot_potato = int(input())
turn = 1

while len(kids) > 1:
    current_kid = kids.popleft()

    if turn != hot_potato:
        kids.append(current_kid)
        turn += 1
    else:
        print(f"Removed {current_kid}")
        turn = 1
print(f"Last is {kids.popleft()}", end="")
