from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])
initial_worms_count = len(worms)
matches_count = 0

while worms and holes:

    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        worms.pop()
        holes.popleft()
        matches_count += 1

    else:
        worms[-1] -= 3
        holes.popleft()

        if worms[-1] <= 0:
            worms.pop()

if matches_count:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if not worms and initial_worms_count == matches_count:
    print("Every worm found a suitable hole!")
elif not worms and initial_worms_count != matches_count:
    print("Worms left: none")

if worms:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")