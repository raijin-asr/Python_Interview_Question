
# define a function to find the elements that can make target sum
def find_sum(numbers, target):

    # initialize the temporary list to avoid duplicates
    temp_list = []

    # loop through the list
    for num in numbers:
        
        # if the difference of target and current element
        # is in the temporary list,
        # print the difference and the current element
        if target - num in temp_list:
            print(target-num, num)

        # add the current element to the temporary list
        temp_list.append(num)


# call the function
numbers = [1, 5, 6, 3, 2, 4]
target_sum = 7
find_sum(numbers, target_sum)