# define a function that returns
# index list of uppercase letters in a string
def uppercase_indexes(string):

    # initialize an empty list
    index_list = []

    # loop through the string using enumerate
    # so that we can get the index of the letter and the letter itself
    for index, letter in enumerate(string):

        # if the letter is in uppercase, add the index to the list
        if letter.isupper():
            index_list.append(index)

    # return the list of indexes
    return index_list


# call the function
indexes = uppercase_indexes('heLLo')
print(indexes)