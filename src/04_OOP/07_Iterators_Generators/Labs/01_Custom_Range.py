class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current_index = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end > self.current_index:
            self.current_index +=1
            return self.current_index
        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)