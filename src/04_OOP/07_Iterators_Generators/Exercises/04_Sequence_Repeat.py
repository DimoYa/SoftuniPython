class sequence_repeat:
    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.len = len(self.text)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.num:
            index = self.current % len(self.text)
            self.current += 1
            return self.text[index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

