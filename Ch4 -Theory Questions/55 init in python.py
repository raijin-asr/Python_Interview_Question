# What is __init__ in Python?
# In Python, __init__() is a special method that works as a constructor for classes. This method is called automatically when we create an object of a class.

# Usually, all the declarations and initializations are done in this method. We do not need to call this method explicitly.

# Let's take a look at an example,
class Person:
    def __init__(self):
        print('inside __init__ method')
 
obj = Person()
 
# Output:
# inside __init__ method

# As you can see, we didn't manually call the __init__() method. The method is called automatically when we create an object of that class.

# Note: The __init__() method is also called a 'constructor' because it is used to construct the object.