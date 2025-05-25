from collections import deque

contestants = deque([int(el) for el in input().split()])
pies = [int(el) for el in input().split()]

while contestants and pies:
    current_contestant = contestants[0]
    current_pie = pies[-1]

    if current_contestant >= current_pie:
        difference = current_contestant - current_pie
        pies.pop()
        contestants.popleft()
        if difference > 0:
            contestants.append(difference)
    else:
        difference = current_pie - current_contestant
        if difference > 1 or len(pies) == 1:
            pies.pop()
            pies.append(difference)
        else:
            pies.pop()
            pies[-1] += difference
        contestants.popleft()

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(el) for el in contestants])}")
elif not pies and not contestants:
    print("We have a champion!")
elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(el) for el in pies])}")
