# What is List Comprehension?
# In Python, list comprehension is an efficient way of defining and creating lists. For example,

word = 'Programiz'
 
# create a list of all the letters of the word
# by using list comprehension
letters = [letter for letter in word]
print(letters)
 
# Output: ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

"""
Here, we can do the same task using a for loop. However, the use of list comprehension makes our code more compact.

Also, list comprehension is faster than a for loop because the for loop uses an individual append() function to append each item into a list. But a list comprehension collects all the elements at once and appends them together.

List comprehensions are also called one-liners, as they are done in just one line."""