from collections import deque

n = int(input())
travel_info = deque()
left_petrol = 0
current_station = 0

for i in range(n):
    travel = [int(item) for item in input().split()]
    travel_info.append(travel)

travel_info_copy = travel_info.copy()

while travel_info_copy:
    amount, distance = travel_info_copy.popleft()
    left_petrol += amount
    if left_petrol >= distance:
        left_petrol -= distance
    else:
        travel_info.rotate(-1)
        travel_info_copy = travel_info.copy()
        current_station += 1
        left_petrol = 0
print(current_station)
