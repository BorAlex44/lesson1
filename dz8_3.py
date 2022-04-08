from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        """qwe"""
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """this shows only with 'from functools import wraps'"""
    return list(map(lambda x: x ** 3, args))

num = calc_cube(5, 7, 9)
print(num)
print(calc_cube.__name__)
print(calc_cube.__doc__)
