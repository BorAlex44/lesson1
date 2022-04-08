from functools import wraps


def val_checker(func_filter):

    def checker(func):
        @wraps(func)
        def decor(x):
            if func_filter(x):
                return func(x)
            else:
                raise ValueError(f'ValueError: wrong val {x}')
        return decor
    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """calc_cube desc"""
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
