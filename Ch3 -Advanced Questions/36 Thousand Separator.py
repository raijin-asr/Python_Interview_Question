
# define a function that adds comma as a thousand separator
def thousand_seperator(number):

    # convert the number to string and reverse it
    number = str(number)[::-1]

    # create an empty string to store the result
    separated = ''

    # start the loop from 0 to length of the passed number
    for i in range(0, len(number)):

        # if the index is not first and is divisible by 3,
        if i != 0 and i %3==0:

            # add a comma to the separated string
            separated+= ","

        # add the number to the separated string
        separated+=number[i]

    # reverse the separated string again and return it
    return separated[::-1]


# call the function and print the result
result = thousand_seperator(100000)
print(result)