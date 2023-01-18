fib_sequence = [0, 1, 1]

target = int(input('Which number from Fibonacci Sequence do you want to see? '))

while len(fib_sequence) < target + 1:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

if target <= (len(fib_sequence) - 1):
    print(f'Requested number is {fib_sequence[target]}')
else:
    iteration = iter(fib_sequence)
    index = 0
    while index != target + 1:
        result = next(iteration)
        index += 1
    print(f'Requested number is {result}')
