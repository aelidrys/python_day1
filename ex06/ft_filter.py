
class ft_filter:
    def __init__(self, fun, iterable):
        self.index = 0
        self.res = []
        for itr in iterable:
            try:
                if fun(itr):
                    self.res.append(itr)
            except TypeError as e:
                raise TypeError(e)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.res):
            result = self.res[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    


def isEven(number):
    if number % 2 == 0:
        return True



data = {"r": 1, "a": 2, "b": 3, "c": 4, "d": 5, "e": 6, "f": 7, "g": 8}
# data = [1, 2, 3, 4, 5, 6, 7, 8]
res = filter(isEven, data)
print("Using filter:")
print(f"res: {res}")
# for elm in res:
#     print(elm)

print("\nUsing ft_filter:")
res = ft_filter(isEven, data)
print(f"res: {res}")
for elm in res:
    print(elm)