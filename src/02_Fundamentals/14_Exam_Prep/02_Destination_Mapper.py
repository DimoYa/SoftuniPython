import re

line = input()

pattern = r"(=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1"

matches = re.finditer(pattern, line)

destinations = [math.group('destination') for math in matches]

travel_points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")