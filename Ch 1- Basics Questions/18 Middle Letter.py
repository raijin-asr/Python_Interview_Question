
# define a function that returns
# the middle letter of the string
def middle_letter(string):

    # if the length of the string is even
    # return the empty string
    if len(string)%2==0:
        return " "

    # else, find the middle index of the string
    middle_index = len(string)//2

    # return the middle letter of the string
    letter = string[middle_index]
    return letter

# call the function
letter = middle_letter('hello')

# print the middle letter
print(letter)