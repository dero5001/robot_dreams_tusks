def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


factorial_number = int(input('Please input the number from which you want to find the factorial '))
result = factorial(factorial_number)

print(f'Your answer is {result}')
