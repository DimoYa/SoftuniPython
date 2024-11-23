class reverse_iter:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # Start from the end of the list

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.data[self.index]  # Return the current item
        raise StopIteration  # Stop when no items are left


# Example usage
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
