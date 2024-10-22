"""What are Python Generators?
Python generators are a simple way of creating iterators. All the work we mentioned above is automatically handled by generators in Python.

To build an iterator in Python manually, we need to

write the __iter__() and __next__() method to keep track of internal states,
and raise StopIteration when there are no values to be returned.
This is both lengthy and counterintuitive. The generator comes to the rescue in such situations.

To create generators, we use the yield keyword instead of the return keyword. We can have as many yield statements as we want and each yield is returned in the next iteration.

Let's take a look at an example"""

def my_gen():
    n = 1
    yield n
 
    n += 1
    yield n
 
    n += 1
    yield n
 
for item in my_gen():
    print(item)

# Here, we've created a function that yields multiple values and each yield value is returned in the next iteration serially.