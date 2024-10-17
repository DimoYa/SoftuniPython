from collections import deque

contestants = deque([int(el) for el in input().split()])
pies = [int(el) for el in input().split()]

while contestants and pies:

    current_contestants = contestants[0]
    current_pie = pies[-1]

    if current_contestants >= current_pie:
        contestants[0] -= current_pie
        if contestants[0] == 0:
            contestants.popleft()
        pies.pop()
    else:
        pies[-1] -= current_contestants
        if pies[-1] == 1 and len(pies) > 1:
            pies.pop()
            pies[-1] += 1
        contestants.popleft()

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")
elif not pies and not contestants:
    print("We have a champion!")
else:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")
