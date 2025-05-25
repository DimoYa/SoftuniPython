import re

line = input()
pattern = r"([=\/])(?P<place_name>[A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, line)
places_result = []
points = 0

places = [math.groupdict() for math in matches]

for place in places:
    place_name = place['place_name']
    places_result.append(place_name)
    points += int(len(place_name))

print(f"Destinations: {', '.join(places_result)}")
print(f"Travel Points: {points}")