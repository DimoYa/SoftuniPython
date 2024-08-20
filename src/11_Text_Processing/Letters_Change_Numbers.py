def get_letter_position(char):
    if char.isupper():
        result = ord(char) - ord('A') + 1
        return result
    elif char.islower():
        result = ord(char) - ord('a') + 1
        return result


line = input().split()
output = 0


for word in line:
    first_letter = word[0]
    number = int(word[1:-1])
    last_letter = word[-1]

    if first_letter.isupper():
        number = number / get_letter_position(first_letter)
    elif first_letter.islower():
        number = number * get_letter_position(first_letter)

    if last_letter.isupper():
        number -= get_letter_position(last_letter)
    elif last_letter.islower():
        number += get_letter_position(last_letter)

    output += number

print(f"{output:.2f}")
