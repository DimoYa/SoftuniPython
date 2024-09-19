from collections import deque

colors = deque(input().split())

main_colors = (
    "red",
    "yellow",
    "blue"
)

secondary_colors = (
    "orange",  # red + yellow = orange
    "purple",    # red + blue = purple
    "green"   # yellow + blue = green
)

collected_colors = []

while colors:

    start = colors.popleft()
    end = colors.pop() if colors else ''

    if start + end in main_colors or start + end in secondary_colors:
        collected_colors.append(start + end)

    elif end + start in main_colors or end + start in secondary_colors:
        collected_colors.append(end + start)

    else:
        start = start[:-1]
        end = end[:-1]
        if len(start) > 0:
            colors.insert(len(colors) // 2, start)
        if len(end) > 0:
            colors.insert(len(colors) // 2, end)

for color in list(collected_colors):
    if color == "orange" and ("red" not in collected_colors or "yellow" not in collected_colors):
        collected_colors.remove("orange")
    elif color == "purple" and ("red" not in collected_colors or "blue" not in collected_colors):
        collected_colors.remove("purple")
    elif color == "green" and ("yellow" not in collected_colors or "blue" not in collected_colors):
        collected_colors.remove("green")

print(collected_colors)
