#Approach 1:
# define a list
numbers = [51, 51, 23, 6, 5, 2]

# initialize the second largest element
second_largest = 0

# sort the numbers in descending order
numbers.sort(reverse=True)

# compare elements next to each till we find different elements
for i in range(len(numbers)):
    
    # if the current element and next element are the same,
    # then continue the loop
    if numbers[i] == numbers[i+1]:
        continue
    
    # if the current and next element is not the same,
    # then next element is the second largest element
    second_largest = numbers[i+1]

    # terminate the loop
    break
    
# print the second largest element
print(second_largest)


# APPROACH 2:------------------
# replace ___ with your code

# define a list
numbers = [51, 51, 23, 6, 5, 2]

# remove duplicate elements from the list
# by converting it to a set
number_set = set(numbers)

# convert the set back to a list
numbers = list(number_set)

# remove max element of the list
max_number = max(numbers)
numbers.remove(max_number)

# access the new maximum element of the list
# which is the second largest element of the original list
largest_number = max(numbers)

print(largest_number)