import re

numbers = input()

pattern = r"\+359([ | -])2\1\d{3}\1\d{4}\b"

matches = [obj.group() for obj in re.finditer(pattern, numbers)]

print(", ".join(matches))
