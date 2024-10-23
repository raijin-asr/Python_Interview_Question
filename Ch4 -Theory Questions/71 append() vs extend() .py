"""Differentiate Between the append() Method and the extend() Method
Both methods are used with lists in Python. Both methods add elements at the end of a list.

append() - is used to add an element at the end of the list.
extend() - is used to add elements at the end of the list from another list.
Take a look at an example,"""
# original list
lst1 = [4, 3, 2, 5, 1, 6]
print(lst1)    # [4, 3, 2, 5, 1, 6]

# append an element
lst1.append(9)
print(lst1)    # [4, 3, 2, 5, 1, 6, 9]

# extend another list
lst2 = [0, 8, 7]
lst1.extend(lst2)
print(lst1)    # [4, 3, 2, 5, 1, 6, 9, 0, 8, 7]