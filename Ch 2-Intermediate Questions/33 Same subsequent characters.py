
# define a function that returns the letter
# that has the same subsequent letter
def same_subsequent(string):

    # start loop from 0 to length of the string
    for i in range(0,len(string)):

        # if the letter at the current index of the string is
        # equal to the letter at next index of the string
        if string[i] == string[i+1]:

            # return letter at the current index of string
            return string[i]


# call the function
letter = same_subsequent('hello')
print(letter)