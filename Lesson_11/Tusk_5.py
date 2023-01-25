# We are improving tusk 1 from lesson 9
def fib_gen(target_number):
    num1 = 0
    num2 = 1
    count = 1

    while count < target_number:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1
        yield num2, count


target = input('Which number from Fibonacci Sequence do you want to see? ')
try:
    if int(target) == 0:
        print('Requested number is 0')
    elif int(target) == 1:
        print('Requested number is 1')
    else:
        for item in fib_gen(int(target)):
            if item[1] == int(target):
                print(f'Requested number is {item[0]}')
                break
except ValueError:
    print('You have to input only numbers, please try again')
