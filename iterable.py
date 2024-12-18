# 1.iter orqali
#1.1
a = [1,2,3,4,5,6,78]
a_iter = iter(a)
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))

#1.2
b = [3,32,5,4,3]
b_iter = iter(b)
print(next(b_iter))
print(next(b_iter))
print(next(b_iter))
print(next(b_iter))
print(next(b_iter))

# 2.OOP orqali
#2.1
class Counter:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start < self.stop:
            return self.start
        raise StopIteration


for elem in Counter(3, 7):
    print(elem)

#2.2
class ReverseCounter:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.stop -= 1

        if self.start < self.stop:
            return self.stop
        raise StopIteration


for elem in ReverseCounter(3, 7):
    print(elem)


# 3.yield orqali
#3.1
def try_generator(y):
    n = y
    n += 1
    yield n
    n *= 2
    yield n
    n += 10
    yield n

result = try_generator(3)
print(next(result))
print(next(result))
print(next(result))

#3.2
def try_generator2(y):
    n = y
    n -= 1
    yield n
    n *= 2
    yield n
    n += 5
    yield n

result = try_generator2(3)
print(next(result))
print(next(result))
print(next(result))

#4.generator orqali
#4.1
def for_generator(start,stop):
    for i in range(start,stop):
        yield i

result1 = for_generator(3,6)
for item in result1:
    print(item)

#4.2
def for_generator2(start,stop):
    for i in range(start,stop):
        yield i * 2

result2 = for_generator2(3,6)
for item in result2:
    print(item)