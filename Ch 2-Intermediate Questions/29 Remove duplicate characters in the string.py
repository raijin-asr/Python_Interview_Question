
# define a function to remove duplicate characters from a string
def remove_duplicates(string):

    # create a new_string variable to store strings without duplicate characters
    new_string = ""

    # loop through each character in the string
    for char in string:

        # if the character is not in the new_string variable, add it to the new_string variable
        if char not in new_string:
            new_string += char

    # print the new_string variable
    print(new_string)


# call the function
text1 = '12stars23'
remove_duplicates(text1)