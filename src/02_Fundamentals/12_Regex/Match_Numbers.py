import re

numbers = input()

pattern = r"(?<!\S)-?(?:0|[1-9]\d*)(?:\.\d+)?(?!\S)"

matches = [obj.group() for obj in re.finditer(pattern, numbers)]

print(" ".join(matches))
