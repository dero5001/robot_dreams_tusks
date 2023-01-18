from time import ctime


def func_decorator(func):
    def inside_func(*args, **kwargs):
        func(*args, **kwargs)
        with open("decorator_info.txt", 'a') as file:
            file.write(f'The function {func} was called at {ctime()}\n')
    return inside_func


@func_decorator
def hello_func():
    print('Hello World!')


@func_decorator
def goodbye_func():
    print('Goodbye!')


hello_func()
goodbye_func()
