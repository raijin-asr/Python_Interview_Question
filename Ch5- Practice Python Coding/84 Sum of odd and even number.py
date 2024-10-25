# Complete the code below

# define a function
def sum_of_odd_and_even(lst):

    odd_sum=0
    even_sum=0
    for i in lst:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
    return odd_sum,even_sum

# call the function
lst = input().split()
int_list = [int(x) for x in lst]
result = sum_of_odd_and_even(int_list)
print(result)