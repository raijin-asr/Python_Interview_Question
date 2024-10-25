# Complete the code below

# define a function
def is_armstrong(number):

    number= str(number)
    sum=0
    for ch in number:
        sum+= pow(int(ch),3)

    if sum==int(number):
        return "It is an Armstrong Number"

    else:
        return "It is not an Armstrong Number"

# call the function
number = input()
result = is_armstrong(number)
print(result)