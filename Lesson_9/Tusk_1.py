fib_sequence = [0, 1, 1]


def fib_gen(sequence_end, list):
    while len(list) <= sequence_end:
        list.append(list[-1] + list[-2])
        yield list[-1]


target = int(input('Which number from Fibonacci Sequence do you want to see? '))

if target <= (len(fib_sequence) - 1):
    print(f'Requested number is {fib_sequence[target]}')
else:
    fib_generator = fib_gen(target + 1, fib_sequence)
    for item in fib_generator:
        if len(fib_sequence) == target + 1:
            print(f'Requested number is {fib_sequence[target]}')
            break
