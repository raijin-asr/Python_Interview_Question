
# define a function thaat finds the smallest missing number
# in a list to make sequence continuous
def find_smallest_missing(lst):

    # fist of all sort the list
    sorted(lst)

    # loop through the list using enumerate so that
    # we can get the index and the element
    for index, element in enumerate(lst):

        # if adding 1 to current element makes the next element,
        # continue the loop as the sequence is continuous
        if lst[index]+1==lst[index+1]:
            continue

        # but if it doesn't,
        # return the value after adding 1 to the current element
        else:
            return lst[index]+1


# call the function
numbers = [2, 4, 6, -1, 5, 1, 0]
missing_number = find_smallest_missing(numbers)
print(missing_number)