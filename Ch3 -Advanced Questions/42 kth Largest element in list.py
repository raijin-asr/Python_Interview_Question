
# define a function that finds the kth largest
# element in a list of integers
def kth_largest_element(nums_list, k):

    # loop timer is how many times we are
    # planning to run loop i.e. k - 1 times
    loop_timer = k-1

    # keep only unique elements in a list using set and function
    # then again converting the set to list
    unique_numbers = list(set(nums_list))

    # run the loop till loop_timer is 0
    while loop_timer >0:

        # find the current maximum element in the list
        # and remove it from the list
        current_maximum = max(unique_numbers)
        unique_numbers.remove(current_maximum)

        # decrement the loop_timer once more
        loop_timer -=1

    # after removing all the maximum elements from the list
    # till 1 less than k times,
    # the current maximum element is the kth largest element
    kth_largest = max(unique_numbers)
    print(kth_largest)


# call the function
numbers = [2, 3, 1, 5, 6, 4]
k = 3
kth_largest_element(numbers, k)