#!/usr/bin/python3

""""""


class CountedIterator():
    """"""
    def __init__(self, somedata):
        self.iterator = iter(somedata)
        self.__counter = 0
        pass

    def get_count(self):
        """"""
        return self.__counter
    
    def __next__(self):
        """"""
        self.__counter += 1
        return next(self.iterator)
    

data = [1, 2, 3, 4, 5]
counted_iterator = CountedIterator(data)

try:
    while True:
        item = next(counted_iterator)
        print(f"Got {item}, total {counted_iterator.get_count()} items iterated.")
except StopIteration:
    print("No more items.")