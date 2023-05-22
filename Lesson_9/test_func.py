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


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


def test_factorial():
    assert factorial(7) == 5040
    assert factorial(5) == 120
    print ('Factorial test OK')


def test_fibonachi():
    sequence = (5, 6, 7, 8, 9)
    answer = (5, 8, 13, 21, 34)
    for i in range(0,5):
        assert rec_fibonacci(sequence[i]) == answer[i]
    print ('Fibonachi test OK')


if __name__ == '__main__':
    test_fibonachi()
    test_factorial()

