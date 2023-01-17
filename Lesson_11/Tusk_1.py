from time import ctime


def func_decorator(func):
    def inside_func(*args, **kwargs):
        print(f'You call the function {func}')
        func(*args, **kwargs)
        print(f'This function was called at {ctime()}')
    return inside_func


@func_decorator
def hello_func():
    print('Hello World!')


@func_decorator
def goodbye_func():
    print('Goodbye!')

