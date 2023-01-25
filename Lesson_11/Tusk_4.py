try:
    print('=' * 10)
    a = int(input('Please input first number that you want to sum '))
    b = int(input('Please input second one '))

except Exception as error:
    print(f'"""{error}""" error occured. Try again')
else:
    print(f'Sum is {a + b}')
finally:
    print('=' * 10)