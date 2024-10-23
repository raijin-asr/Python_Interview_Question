"""Explain Type Casting in Python
In Python, type casting refers to the technique of changing data from one type to another.

That means we can cast integer data to a string and numeric strings to integers. We can cast strings to booleans and vice versa. And so on.

Let's take a look at an example,"""
x = 5
print(x, ' - ', type(x))  # 5 - <class 'int'>

x = str(x)
print(x, ' - ', type(x))  # 5 - <class 'str'>

x = bool(x)
print(x, ' - ', type(x))  # True - <class 'bool'>

x = int(x)
print(x, ' - ', type(x))  # 1 - <class 'int'>

x = float(x)
print(x, ' - ', type(x))  # 1.0 - <class 'float'>

# Here, we have first declared x variable with integer data. Then we cast that value to string, boolean, integer, and float types, respectively.

# The values are automatically converted according to the specified data types.