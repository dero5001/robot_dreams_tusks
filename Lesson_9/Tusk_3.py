def rec_fibonacci(target_number, num1 = 0, num2 = 1, count = 1):

    if target_number == 0:
        return num1
    elif target_number == 1:
        return num2

    if count < target_number:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count += 1
        return rec_fibonacci(target_number, num1, num2, count)
    else:
        return num2


target = int(input('Which number from Fibonacci Sequence do you want to see? '))


result = rec_fibonacci(target)
print(f'Requested number is {result}')
