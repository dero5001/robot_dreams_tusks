class MyCtxManager:

    def __enter__(self):
        print('=' * 10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_val)
        print('=' * 10)


def sum():
    a = int(input('Please input first number that you want to sum '))
    b = int(input('Please input second one '))
    print(f'Sum is {a + b}')


with MyCtxManager():
    sum()
