"""What is self in Python?
In Python, whenever we call methods by its object, that object is automatically passed as a parameter. So, the self variable represents the instance of the class (object).

However, self is not a keyword, but it is a convention since it makes sense. Let's look at an example,"""

class Person:
    def __init__(self, age):
        self.age = age
 
    def get_age(self):
        print(self.age)
 
 
p = Person(45)
p.get_age()

# Take a look at the methods in the Person class above. Every method has the first parameter as self, in which the current instance of the class is passed.

# In this case, the object p itself is passed while calling the get_age() method.