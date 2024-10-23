# Explain the Use of any() and all() in Python
# In Python, any() is an inbuilt function that returns True if any of the values in the passed iterable object is True. Else, it returns False. For example,

values = [True, True, True]
print(any(values))  # True
 
values = [False, False, False]
print(any(values))  # False
 
values = [True, False, True]
print(any(values))  # True

# Similarly, the all() function in Python returns True only if all the values in the passed iterable object are True. For example,
values = [True, True, True]
print(all(values))  # True
 
values = [False, False, False]
print(all(values))  # False
 
values = [True, False, True]
print(all(values))  # False