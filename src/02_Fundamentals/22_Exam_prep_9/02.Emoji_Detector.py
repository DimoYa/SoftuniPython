import re

line = input()
pattern_emoji = r"(:{2}|\*{2})(?P<word>[A-Z][a-z]{2,})\1"
pattern_threshold = r"\d+"
matches_emoji = re.finditer(pattern_emoji, line)
matches_threshold = re.finditer(pattern_threshold, line)


cool_threshold = 1
total_emojis = 0
cool_emojis = []

for amount in matches_threshold:
    for digit in amount.group():
        cool_threshold *= int(digit)

for match in matches_emoji:
    word = match.group("word")
    ascii_sum = sum([ord(ch) for ch in word])
    total_emojis += 1

    if ascii_sum >= cool_threshold:
        cool_emojis.append(match.group(0))

print(f"Cool threshold: {cool_threshold}")
print(f"{total_emojis} emojis found in the text. The cool ones are:")
[print(el) for el in cool_emojis]