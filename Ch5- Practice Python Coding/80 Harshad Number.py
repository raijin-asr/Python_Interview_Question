# Complete the code below

# define a function
def is_harshad(number):
    sum=0
    for i in number:
        sum+=int(i)

    if int(number) % sum ==0:
        return "It is a Harshad Number"
    else:
        return "It is not a Harshad Number"


# call the function
number = input()
result = is_harshad(number)
print(result)