# define a function that prints the length of a string without len() function
def length_of_string(string):

    # define a counter that stores the length of a string
    length=0

    # loop through each character in the string
    for char in string:

        # for each character, increment the length counter by 1
        length+=1

    # print the length counter
    print(length)


# call the function
length_of_string('Python')