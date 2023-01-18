class FibIterator:

    count = 1
    num1 = 0
    num2 = 1

    def __init__(self, target_number):
        self.stop = target_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.stop:
            print(f'Requested number is {self.num2}')
            raise StopIteration

        num3 = self.num1 + self.num2
        self.num1 = self.num2
        self.num2 = num3
        self.count +=1


target = int(input('Which number from Fibonacci Sequence do you want to see? '))

fib_sequence = FibIterator(target)
for item in fib_sequence:
    pass
