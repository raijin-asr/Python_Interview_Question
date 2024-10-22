"""What are Python Iterators?
Python iterators are objects that allow us to iterate over the iterables (lists, sets, tuples, etc.) and get data one at a time.

Iterators provide __iter__() and __next__() methods with which we can create our own custom loops.

__iter__() - returns an iterator object
__next__() - accesses the next data from an iterable"""

class Numbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            temp = self.num
            self.num += 1
            return temp
        else:
            raise StopIteration


obj = iter(Numbers())

for o in obj:
    print(o)

"""
Here, we've created a class, and inside the class, there are two methods __iter__() and __next__().

1. __iter__() Method

returns an iterator object
is called when we create an object of iterable
2. __next__() Method

returns the next value starting from num = 1 to 5
if num is greater than 5, the StopIteration exception will stop the execution.
Hence, we can successfully implement a loop using an iterator."""