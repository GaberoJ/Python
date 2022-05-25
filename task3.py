def type_logger(func):
    def wrapper(*args):
        result = []
        func(*args)
        for arg in args:
            result.append(f'{arg} {type(arg)}, value = {func(arg)}')
        return result
    return wrapper


@type_logger
def calc_cube(*args):
    list_of_cubes = [x ** 3 for x in args]
    return list_of_cubes


print(calc_cube(5, 8, 9.7))
