from time import ctime


def func_decorator(func):
    def inside_func(*args, **kwargs):
        print(f'You call the function {func}')
        result = func(*args, **kwargs)
        print(f'This function was called at {ctime()}')
        return result
    return inside_func


@func_decorator
def hello_func():
    print('Hello World!')


@func_decorator
def sum_func(*args):
    result = 0
    for i in args:
        result += i
    print(result)


hello_func()
sum_func(10, 1, 5, 15)
