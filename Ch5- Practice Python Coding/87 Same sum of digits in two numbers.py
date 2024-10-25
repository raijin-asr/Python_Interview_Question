# Complete the code below

# define a function
def is_equal(first_number, second_number):

    sum_first=0
    sum_second=0
    for i in str(first_number):
        sum_first+=int(i)

    for j in str(second_number):
        sum_second+=int(j)

    if sum_first==sum_second:
        return True
    else: 
        return False

# call the function
first_number = input()
second_number = input()
result = is_equal(first_number, second_number)
print(result)