# 

def liner(func):
    def inner():
        print('----------')
        func()
        print('----------')

    return inner

# Here, when the value of a is changed to string, Python automatically converts the data type of a to str from int.

# This is the reason Python is called a weakly-typed language

a = 5
print(a, type(a))
 
a = 'John'
print(a, type(a))
 
# Output:
# ------------
# 5 <class 'int'>
# John <class 'str'>
