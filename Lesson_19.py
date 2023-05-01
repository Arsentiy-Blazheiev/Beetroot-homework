# Task 1

def with_index(iterable, start=0):
    n = start
    for i in iterable:
        yield n, i
        n += 1


my_list = [1, 2, 3, 4]
print(list(with_index(my_list, 1)))

# Task 2


def in_range(start, end, step=1):
    my_list = []
    i = start
    if step < 0:
        while i > end:
            my_list.append(i)
            i += step
    if step > 0:
        while i < end:
            my_list.append(i)
            i += step
    if step == 0:
        raise ValueError("Крок не повинен бути 0")
    return my_list


print(in_range(1, 10, 1))
print(in_range(-1, -10, -1))

# Task 3


class Iter:
    def __init__(self, data):
        self.data = data
        self. index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            result = self.data[self.index]
            self.index += 1
            return result

    def __getitem__(self, index):
        return self.data[index]


my_iter = Iter([1, 2, 3, 4, 5, 6, 7])
for i in my_iter:
    print(i)
