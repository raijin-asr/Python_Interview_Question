
# define a function to find the before and after of a given number
def before_and_after(n):

    # decrement the number by 1 to find the before number
    before = n-1

    # increment the number by 1 to find the after number
    after = n+1

    # return the tuple of before, n and after
    return (before,n,after)


# call the function
result = before_and_after(5)
print(result)