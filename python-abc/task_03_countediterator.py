#!/usr/bin/python3

""""""


class CountedIterator():
    """"""

    iterator = iter([])
    counter: int = 0
    def __init__(self, somedata):
        self.iterator = iter(somedata)
        self.counter = 0
        pass

    def __iter__():
        return self

    def get_count(self):
        """"""
        return self.counter
    
    def __next__(self):
        """"""
        try:
            item = next(self.iterator)
            self.__counter += 1
            return item
        except StopIteration as exc:
            raise StopIteration() from exc
    

data = [1, 2, 3, 4, 5]
counted_iterator = CountedIterator(data)

try:
    while True:
        item = next(counted_iterator)
        print(f"Got {item}, total {counted_iterator.get_count()} items iterated.")
except StopIteration:
    print("No more items.")