class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равным 0')
        else:
            self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step < 0 and self.pointer < self.stop or self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        self.pointer += self.step
        return self.pointer - self.step

try:
    iter1 = Iterator(100, 200, 0)
    for value in iter1:
        print(value, end = '')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for value in iter2:
    print(f'{value} ', end = '')
print()
for value in iter3:
    print(f'{value} ', end = '')
print()
for value in iter4:
    print(f'{value} ', end = '')
print()
for value in iter5:
    print(f'{value} ', end = '')
print()
