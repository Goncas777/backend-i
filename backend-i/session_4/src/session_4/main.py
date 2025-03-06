class EvenIterator:
    def __init__(self, numberslist):
        self.numbers = numberslist
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration
    


numlist = [1,2,4,6,3,2,5,2,61,643,32,432,52,1,352,653,23,12]



for num in EvenIterator(numlist):
    print(num)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


maxnumfibo = 12


for num in fibonacci(maxnumfibo):
    print("Fibonacci number:", num)