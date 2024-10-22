"""Differentiate Between == Operator and is Keyword
The == operator is used to compare the value of two objects whereas the is keyword is used to check if two variables point to the same object in memory.

Let's understand this with the help of an example."""

a = [1, 2, 3]
 
b = a
c = a.copy() # creates another instance of same object
 
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(c)  # [1, 2, 3]
 
print(a == b)  # True
print(a == c)  # True
 
print(a is b)  # True
print(a is c)  # False
"""
As you can see, lists b and c have the same value as list a. But in memory, b points to the original list a, whereas c has a clone of a in another memory location.

Here, because the == operator only checks values, a == b and a == c are True.

However, because the is keyword checks if both variables are pointing to the same memory location, a is b returns True, but a is c returns False."""