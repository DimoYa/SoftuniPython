from collections import deque

quantity = int(input())
deq = deque([int(num) for num in input().split()])

biggest_order = max(list(deq))
print(biggest_order)

while deq and quantity - deq[0] >= 0:
    quantity -= deq.popleft()

if deq:
    print(f"Orders left: {' '.join([str(item) for item in deq])}")
else:
    print("Orders complete")
