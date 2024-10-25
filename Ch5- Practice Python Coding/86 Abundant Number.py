# Complete the code below

# define a function
def is_abundant(number):

    list=[]
    sum=0
    for n in range(1,number):
        if number%n==0 and n!=number:
            list.append(n)
            sum+=n
    if number<sum:
        return "It is an Abundant Number"

    else:
        return "It is not an Abundant Number"

# call the function
number = int(input())
result = is_abundant(number)
print(result)