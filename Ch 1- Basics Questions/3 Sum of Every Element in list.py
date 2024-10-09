# replace ___ with your code

# function to find the sum of all list elements
def find_sum(nums_list):
    
    # variable to store the sum of all elements
    sum = 0

    # access each element of the list using a loop
    for num in nums_list:
        # add every element of the list to sum
        sum+=num

    # return the sum variable
    return sum


# create a list of integers
nums_list = [5, 6, 7, 8, 23, 51]

# call the function to find the sum
sum = find_sum(nums_list)
print(sum)