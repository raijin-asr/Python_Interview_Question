# Does Python Support Multiple Inheritance?
# Yes, Python supports multiple inheritance.

# Take a look at this example,
class Person:
    def can_walk(self):
        print('person can walk')
        
class Student:
    def can_study(self):
        print('Student can study')
        
 
class Boy(Person, Student):
    pass
 
 
b = Boy()
b.can_walk()
b.can_study()

# Here, Person and Student are two separate classes. But the Boy class is inherited from both the Person and Student classes.