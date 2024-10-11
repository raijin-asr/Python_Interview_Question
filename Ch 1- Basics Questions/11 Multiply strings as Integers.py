# define a function that takes numeric strings as parameter
# and returns the product of it in string format
def multiply(string1, string2):

    # convert the strings to integers
    num1 = int(string1)
    num2 = int(string2)

    # multiply the numbers
    product = num1*num2

    # convert the product to string
    string_product = str(product)

    # print the product
    print(string_product)


# call the function
multiply('10', '20')