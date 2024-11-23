class vowels:
    def __init__(self, text):
        self.text = text
        self.vow_w = [w for w in self.text if w.lower() in ["a", "e", "i", "o", "u", "y"]]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.vow_w):
            current_vowel = self.vow_w[self.index]
            self.index += 1  # Move to the next vowel
            return current_vowel
        raise StopIteration  # End the iteration when all vowels are exhausted


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
