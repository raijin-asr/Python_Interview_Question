
# define a function that sorts the string and
# appends the sum of numbers if they are present
# in the list
def sort_alphabets(string):

    # define empty string and list
    # to store alphabets and numbers
    new_string = ''
    numbers = []

    # loop through the string
    for char in string:

        # if the character is a number
        # convert character to integer and
        # append it to the numbers list
        if char.isdigit():
            numbers.append(int(char))

        # if the character is not a number
        # append the character to the new string
        else:
            new_string+=char

    # sort the new string
    new_string = sorted(new_string)

    # sorting the string gives us a list
    # so we can use join() function to join
    # the list to a string
    new_string = "".join(new_string)

    # calculate sum of numbers in the list
    sum_numbers = sum(numbers)

    # now, append sum of numbers to the new string
    # by converting the sum to string
    final_string = new_string + (str(sum_numbers))

    # print the final string
    print(final_string)


# call the function
sort_alphabets('9python123')