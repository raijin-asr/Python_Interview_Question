
# define a function that converts the snake case to the pascal case
def pascal_case(string):

    # initialize the variables to store parsed string and the counter to count string characters
    new_string = ''
    i = 0

    # run loop from 0 to the length of the string
    while i < len(string):

        # if the first character is a lowercase letter, add an uppercase letter
        if i == 0 and string[i].islower():
            new_string += string[i].upper()

        # if the current character is an underscore, convert the next character to uppercase and add
        elif string[i]== "_":
            new_string += string[i+1].upper()

            # also increase the counter by 1 since the next character is already passed here
            i+=1

        # else, add the character as it is
        else:
            new_string += string[i]

        # increase the counter by 1
        i+=1

    # return the new string
    return new_string


# call the function
result = pascal_case('custom_date_builder')
print(result)