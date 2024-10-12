# define a function that can add any number of arguments
def adder(*args):

    # initialize the sum variable
    sum = 0

    # loop through the arguments and add them to the sum variable
    for arg in args:
        sum+=arg

    # print the sum
    print(sum)


# call the function
adder(1, 2, 3, 4, 5)