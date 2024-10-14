
# define a function that checks if a
# letters in a list can make a given string
def can_make(lst, string):

    # loop through each character in a string
    for char in string:

        # if a character is not in a list, return False
        if char not in lst:
            return False

    # if all characters are in a list, return True
    return True


# create the list and the string
lst = ['a', 'l', 'p', 'c', 'e', 'd']
string = 'apple'

# call the function
result = can_make(lst, string)

# print the result
print(result)