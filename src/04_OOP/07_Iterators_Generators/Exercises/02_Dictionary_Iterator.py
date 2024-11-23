class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = iter(dictionary)  # Create an iterator for the keys

    def __iter__(self):
        return self

    def __next__(self):
        try:
            key = next(self.keys)  # Get the next key
            return key, self.dictionary[key]
        except StopIteration:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
