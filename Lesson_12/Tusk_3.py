from time import ctime


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        with open('custom_exception_info.txt', 'w+') as file:
            file.write(f'The "{self.message}" exception arised at {ctime()}\n')
    pass


raise MyCustomException('Custom exception is occured')
