
# define a function that finds the
# first and last occurences of target element in a list
def first_and_last(num_list, target_element):

    # initialize variables for first and last indexes
    first = 0
    last = -1

    # loop through the list using enumerate function
    # so that we can also access index
    for ind, elem in enumerate(num_list):

        # if the target element is found
        if target_element==elem:

            # if first index is not set for first time,
            # then only set it to the current index
            if first == 0:
                first=ind

            # set the last index to the current index
            # every time the target element is found
            last=ind

    # return the first and last indexes as tuples
    return (first,last)


# call the function
numbers = [1, 5, 6, 7, 8, 2, 7, 9, 1]
target = 7
result = first_and_last(numbers, target)
print(result)