# Complete the code below

# define a function
def is_sequence(number_list):

    for i in range(len(number_list)):
        if number_list[i] < number_list[i+1]:
            return True
        else:
            return False


# call the function
number_list = input().split()
result = is_sequence(number_list)
print(result)