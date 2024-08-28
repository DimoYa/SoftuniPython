import re

line = input()

pattern = r"([= | /])(?P<destination>[A-Z][A-Za-z]{2,})\1"


matches = [obj.group('destination') for obj in re.finditer(pattern, line)]


print(f"Destinations: {', '.join(matches)}")

travel_points = sum(len(destination) for destination in matches)
print(f"Travel Points: {travel_points}")
