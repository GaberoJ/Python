def val_checker(value):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not value(arg):
                    raise ValueError(f'wrong value {arg}')
            result = func(*args)
            return result
        return wrapper
    return decorator


@val_checker(lambda x: 0 < x <= 10)
def calc_cube(x):
    return x ** 3


print(calc_cube(7))
print(calc_cube(-5))
