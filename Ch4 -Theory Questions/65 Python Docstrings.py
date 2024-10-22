"""Explain Python Docstrings and How We Can Create Them?
Docstring is the comment written immediately after a function or class definition. It is ignored by the interpreter in the same way as comments are ignored.

Docstrings are normally written to explain the definition and input/output parameters. We enclose docstrings inside a pair of 3 single quotes ''', as shown below."""

def double_number(n):
    '''Takes in a number n, returns n*2'''
    return n*2
 
print(double_number.__doc__)

# Here, we can see that the __doc__ attribute is used to get the docstring content.