# How Can You Read the Content of a File in Python?
# In Python, the open() function returns a file object. Using open(), we can pass the filename as an argument and mode as an optional argument. For example,

file = open('file.txt')

# Here, we are opening the file.txt file with our program.

# The default mode to open a file is read-only. We can pass r to read, w to write, x to create, and a to append.

# To read a file, we can use the read() method in the file object. Here's how,

file = open('requirements.txt')
content = file.read()
print(content)
file.close()

# This will display the contents of requirements.txt on the terminal.

