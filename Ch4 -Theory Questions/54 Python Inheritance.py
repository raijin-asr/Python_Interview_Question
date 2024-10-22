"""
Explain Python Inheritance
Inheritance is a concept in Object Oriented Programming where one class can inherit the properties and methods of another class.

That means the inherited class can access all methods and properties of the superclass.

Inheritance follows the DRY (Don't Repeat Yourself) principle and reduces the duplication of codes.

In Python, we can inherit one class from another by passing the class name in parentheses while defining the class. Main classes are also called parent classes, whereas inherited classes are called child classes.

Here's an example of Python inheritance,"""

class Person:
    def walks(self):
        print('Person walks')
 
 
class Student(Person):
    def studies(self):
        print('Student studies')
 
 
obj = Student()
obj.walks()
obj.studies()
 
 
# Output:
# Person walks
# Student studies