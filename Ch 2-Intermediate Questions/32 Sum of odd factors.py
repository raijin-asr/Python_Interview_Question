
# function that sums the odd factors of a number
def odd_factor_sum(number):

    # initialize factors list to store all factors
    factors = []

    # start loop from 1 to number
    for i in range(1,number):

        # if the number is divisible by i, add i to the factors list
        if number%i==0:
            factors.append(i)

    # initialize sum to 0
    sum = 0

    # loop through factors list
    for i in factors:

        # if i is odd, add i to sum
        if i%2!=0:
            sum+=i

    # print the sum
    print(sum)


# call the function
num = 18
odd_factor_sum(num)