def make_underline(function):
    def wrapper(*args):
        text = function(*args)
        return f"<u>{text}</u>"
    return wrapper


def make_italic(function):
    def wrapper(*args):
        text = function(*args)
        return f"<i>{text}</i>"
    return wrapper


def make_bold(function):
    def wrapper(*args):
        text = function(*args)
        return f"<b>{text}</b>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
