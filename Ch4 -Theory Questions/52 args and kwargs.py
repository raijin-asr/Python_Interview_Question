# What Are *args and **kwargs in Python?
# In Python, we can take any number of parameters using *args and **kwargs in a function.

# If we use *args as a parameter when defining a function, we can pass any number of positional arguments. All the passed arguments are stored in args as a tuple.

# This comes from the fact that starred expressions * are used for unpacking any iterable objects like lists and tuples. The name 'args' is arbitrary but is used as the standard convention.

# For example,
def fun(*args):
    print(args)
 
 
fun(3, 2, 1)
 
# Output: (3, 2, 1)


"""
Similarly, **kwargs is used to collect any number of keyword arguments and stored as a dictionary in the kwargs variable.

It comes from the fact that ** is used to unpack the key and values of a dictionary. Again, 'kwargs' is an arbitrary name but is the standard convention.

For example,"""
def fun(**kwargs):
    print(kwargs)
 
 
fun(name='john', age=30)
 
# Output: {'name': 'john', 'age': 30}
