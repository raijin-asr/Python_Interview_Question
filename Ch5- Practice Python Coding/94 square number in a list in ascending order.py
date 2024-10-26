# Complete the code below

# define a function
def square_the_lsit(lst):

    square_list= [n**2 for n in lst]
    return sorted(square_list)

# get input for the list
lst = input().split()

# convert list elements to integer
lst = [int(x) for x in lst]

# call the function
result = square_the_lsit(lst)
print(result)