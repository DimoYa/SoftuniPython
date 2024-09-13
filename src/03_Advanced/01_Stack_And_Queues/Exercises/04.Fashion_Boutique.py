clothes = [int(item) for item in input().split()]
rack_capacity = int(input())
used_racks = 1
current_rack = rack_capacity

while clothes:

    if current_rack < clothes[-1]:
        used_racks += 1
        current_rack = rack_capacity

    current_rack -= clothes.pop()

print(used_racks)
