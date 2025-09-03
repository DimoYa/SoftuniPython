import re

line = input()
pattern = r"([:*]{2})(?P<emoji_name>[A-Z][a-z]{2,})\1"
digit = r"\d+"
matches = re.finditer(pattern, line)
digits = re.finditer(digit, line)
emoji_result = {}

cool_threshold = 1
for match in digits:
    number = match.group()
    for digit_char in number:
        cool_threshold *= int(digit_char)

emojis = [match for match in matches]

for emoji in emojis:
    full_match = emoji.group()
    emoji_name = emoji.group('emoji_name')
    coolness = sum(ord(char) for char in emoji_name)
    emoji_result[full_match] = coolness

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_result)} emojis found in the text. The cool ones are:")
print("\n".join([full_match for full_match, ascii_value in emoji_result.items() if ascii_value > cool_threshold]))