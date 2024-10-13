
# given string
sentence = 'python is easy'

# split the string into words
# by default, python splits by space
# and returns a list of splitted elements
words = sentence.split()

# sort the list of words
# sort() is a built-in function and
# it sorts the list in ascending order
words.sort()

# loop through each word and print it
for word in words:
    print(word)