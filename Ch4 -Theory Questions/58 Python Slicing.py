"""What is Slicing in Python?
In Python, slicing is a way of obtaining a part of whole elements from the list.

We can slice strings or lists by adding square brackets [] at the end of the value. Inside [],

the first value is referred to as the start index,
the second value is referred to as the end index,
the last value is referred to as intervals,
and each of these values are separated by the : symbol.

Let's take a look at an example,"""

my_list = [22, 33, 55, 66, 77, 99]
print(my_list[:])   	# prints the whole list
print(my_list[1:3]) 	# prints the elements at indexes 1 and 2
print(my_list[1:5:2])   # prints the elements from index 1 to index 4 with interval of 2
print(my_list[:2])  	# prints the elements up to index 1 inclusive
