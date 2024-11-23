class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start_index = 0 - self.step
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.counter:
            self.start_index += self.step
            self.counter += 1
            return self.start_index
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)