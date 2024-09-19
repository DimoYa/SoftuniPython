from collections import deque

materials = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])

presents = {}

magic_mapper = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic:
    current_magic = materials[-1] * magic[0]

    if current_magic in magic_mapper:
        current_present = magic_mapper[current_magic]

        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1

        materials.pop()
        magic.popleft()

    elif current_magic < 0:
        new_material = materials.pop() + magic.popleft()
        materials.append(new_material)
    elif current_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()

if ("Doll" in presents and "Wooden train" in presents) or ("Bicycle" in presents and "Teddy bear" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

if presents:
    for present, count in sorted(presents.items()):
        print(f"{present}: {count}")
