from time import ctime


class MyCustomException(Exception):
    with open('custom_exception_info.txt', 'w') as file:
        file.write(f'The "{Exception}" exception arised at {ctime()}\n')
    pass


raise MyCustomException('Custom exception is occured')
