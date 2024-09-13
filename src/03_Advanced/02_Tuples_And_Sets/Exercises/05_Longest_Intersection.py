n = int(input())
longest_intersection = set()

for _ in range(n):
    first, second = input().split("-")
    first_start, first_last = [int(item) for item in first.split(",")]
    second_start, second_last = [int(item) for item in second.split(",")]

    first_set = set(range(first_start, first_last + 1))
    second_set = set(range(second_start, second_last + 1))

    intersect_set = first_set.intersection(second_set)

    if len(intersect_set) > len(longest_intersection):
        longest_intersection = intersect_set

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
