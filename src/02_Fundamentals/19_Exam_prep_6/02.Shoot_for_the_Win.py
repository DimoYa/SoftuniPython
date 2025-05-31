target = [int(el) for el in input().split()]
command = input()
shoot_targets = 0

while not command == "End":
    index = int(command)

    if index < 0 or index >= len(target):
        command = input()
        continue

    if target[index] == -1:
        command = input()
        continue

    shot_value = target[index]
    target[index] = -1
    shoot_targets += 1

    for i in range(len(target)):
        if target[i] != -1:
            if target[i] > shot_value:
                target[i] -= shot_value
            else:
                target[i] += shot_value

    command = input()

print(f"Shot targets: {shoot_targets} -> {' '.join([str(el) for el in target])}")