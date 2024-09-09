from collections import deque

line = input()
queue = deque([])

while not line == "End":

    if line == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(line)
    line = input()
print(f"{len(queue)} people remaining.")
