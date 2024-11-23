def vowel_filter(function):

    def wrapper():

        text = function()
        return [w for w in text if w.lower() in "aeiouy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
