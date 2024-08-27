import re

dates = input()

pattern = r"\b(?P<Day>\d{2})(?P<separator>[-|\.|\/])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"

matches = [obj.groupdict() for obj in re.finditer(pattern, dates)]

print("\n".join([f"Day: {data['Day']}, Month: {data['Month']},"
                 f" Year: {data['Year']}" for data in matches]), end="")
