# What is super() in Python?
# The super() method is used to call the parent class's properties from the child class. Using super(), we can invoke any method or constructor of the parent class. For example,

class Person:
    def __init__(self, name):
        self.name = name
 
    def walk(self, to):
        print(self.name, 'is walking to', to)
 
 
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
 
    def go_school(self):
        super().walk(to='school')
 
    def go_home(self):
        super().walk(to='home')
 
 
obj = Student('John')
obj.go_school()
obj.go_home()
 
# Output:
# John is walking to school
# John is walking to home

# Here, we have used super() to call the constructor and methods of the parent class (Person) from the child class (Student).