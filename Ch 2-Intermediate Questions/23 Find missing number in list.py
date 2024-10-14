# replace ___ with your code

# define a list
my_list = [1, 3, 4, 5, 6, 7, 8, 9, 10]

# find the length of the list
n = len(my_list)

# find the total sum till n+1,
# because 1 number is missing
total = ( (n + 1) * (n + 2) ) / 2 

# calculate the sum of current elements
temp_total = sum(my_list)

# find the missing element by 
# subtracting the current sum from the sum that should be
# also convert it to integer
missing_number = int(total- temp_total)

# print the missing number
print(missing_number)