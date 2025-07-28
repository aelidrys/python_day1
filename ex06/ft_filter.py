# mimc filter function using list comprhensions

class ft_filter:

    '''ft_filter(function or None, iterable) --> ft_filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''

    def __init__(self, fun, iterable):
        self.index = 0
        if fun is None:
            self.filtred = [item for item in iterable if item]
        else:
            self.filtred = [item for item in iterable if fun(item)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.filtred):
            raise StopIteration
        item = self.filtred[self.index]
        self.index += 1
        return item


def isEven(number):
    if number % 2 == 0:
        return True


if __name__ == '__main__':

    data = [4, 5, 8, 5, 2, 1, 6]
    res = ft_filter(lambda x: x % 2 == 0, data)
    print(f"res = {res}")

    for elem in res:
        print(f"{elem}")

    res = filter(isEven, data)
    print(f"res = {res}")

    for elem in res:
        print(elem)
