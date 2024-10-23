"""What is Negative Indexing in Python?
The index of an element is the place of the element in any iterable object. If the list is [1, 2, 3], then the index of element 1 is 0. That's because indexes start with 0 in Python.

In the same way, Python also supports negative indexing. Negative indexes start with -1 and references the last element of an object.

For example, if the list is [1, 2, 3], then the index of element 3 is -1, and the index of element 2 is -2."""
lst = ['h', 'e', 'l', 'l', 'o']
 
# positive indexing
print(lst[0])
print(lst[3])
 
# negative indexing
print(lst[-1])
print(lst[-4])