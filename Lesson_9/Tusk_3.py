fib_sequence = [0, 1, 1]


def rec_fibonacci(number, list):
    if len(list) < number + 1:
        list.append(list[-1] + list[-2])
        return rec_fibonacci(number, list)
    else:
        return fib_sequence[number]


target = int(input('Which number from Fibonacci Sequence do you want to see? '))


result = rec_fibonacci(target, fib_sequence)
print(f'Requested number is {result}')
