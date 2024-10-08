# function to find the sum of smallest and largest element
def calc_sum(num_list):
    
    # find the smallest and largest value
    smallest_value = min(num_list)
    largest_value = max(num_list)

    # find the sum of the smallest and largest elements
    total = smallest_value + largest_value

    # return the total
    return total


# list of numbers
numbers = [5, 6, 3, 8, 9]

# call the function to find the sum
result = calc_sum(numbers)

# print the sum
print(result)