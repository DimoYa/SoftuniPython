from collections import deque

packages_stack = [int(x) for x in input().split()]
couriers_deq = deque([int(x) for x in input().split()])
total_delivered_weight = 0

while packages_stack and couriers_deq:
    current_package = packages_stack[-1]
    current_courier_capacity = couriers_deq[0]

    if current_courier_capacity >= current_package:
        couriers_deq.popleft()
        if current_courier_capacity > current_package:
            current_courier_capacity -= 2 * current_package

            if current_courier_capacity > 0:
                couriers_deq.append(current_courier_capacity)
        total_delivered_weight += packages_stack.pop()
    else:
        diff = packages_stack.pop() - couriers_deq.popleft()
        packages_stack.append(diff)
        total_delivered_weight += abs(current_courier_capacity)

print(f"Total weight: {total_delivered_weight} kg")

if not packages_stack and not couriers_deq:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_stack and not couriers_deq:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join([str(el) for el in packages_stack])}")
elif not packages_stack and couriers_deq:
    print(f"Couriers are still on duty: {', '.join([str(el) for el in couriers_deq])}"
          f" but there are no more packages to deliver.")



