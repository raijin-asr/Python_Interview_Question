# What are Python Closures?
# The technique of binding data to a function is called Python Closures. We can achieve this by using nested functions. Let's try to understand by the example below,

def print_msg(msg):
    def printer():
        print(msg)
 
    return printer
 
another = print_msg('Hello')

another() # Hello

# Here, we've bound the msg parameter that is passed in the print_msg() function to the another function.
# By creating the nested function, the printer() function can access variables in the parent function, i.e., print_msg() function.