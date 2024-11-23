def type_check(param_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if not all(isinstance(arg, param_type) for arg in args):
                return "Bad Type"
            return function(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
