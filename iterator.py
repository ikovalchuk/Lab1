import collections.abc

class MyMap(collections.abc.Mapping):
    def __init__(self, n):
        self.n = n

    def __getitem__(self, key):
        if 0 <= key < self.n:
            return key * key
        else:
            raise KeyError('Invalid key')

    def __iter__(self): 
        for x in range(self.n):
            yield x

    def __len__(self):
        return self.n

m = MyMap(5)
for k, v in m.items():
    print(k, '->', v)
# 0 -> 0
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16