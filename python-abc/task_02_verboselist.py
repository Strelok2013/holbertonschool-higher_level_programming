#!/usr/bin/python3
""""""

from typing import Iterable, SupportsIndex


class VerboseList(list):
    """"""

    def append(self, object):
        print("Added [{}] to the list.".format(object))
        return super().append(object)
    
    def extend(self, iterable: Iterable):
        print("Extended the list with [{}] items.".format(len(iterable)))
        return super().extend(iterable)
    
    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)
    
    def pop(self, index: SupportsIndex = -1):
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
    
vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)