# Complete the code below
# MY SOLUTION:

# define a function
def is_lapindrome(number):

    mid_index= len(number)//2
    before_mid= number[:mid_index]
    after_mid= number[mid_index:]

    for i in number:
        if (i in before_mid) == (i in after_mid):
            return "It is Lapindrome Number"

        else:
            return "It is not Lapindrome Number"        


# call the function
number = input()
result = is_lapindrome(number)
print(result)


#PROGRAMIZ SOLUTION:------------------------------
# Complete the code below

# define a function
def is_lapindrome(number):

    # divide the length of the number by 2 to get the middle index
    middle_index = len(number) // 2

    # get the first half of the number
    first_half = number[:middle_index]
    
    
    # if the length of the number is even
    if len(number) % 2 == 0:

        # get the second half of the number
        second_half = number[middle_index:]

    # if the length of the number is odd
    else:

        # get the second half of the number by skipping the middle character
        second_half = number[middle_index + 1 :]

    # sort first_half and second_half
    first_half = ''.join(sorted(first_half))
    second_half = ''.join(sorted(second_half))
    
    # compare the sorted first half with the sorted second half
    # if they are the same, the number is Lapindrome
    # else, they are not Lapindrome
    if first_half == second_half:
        return 'It is Lapindrome Number'
    else:
        return 'It is not Lapindrome Number'


# call the function
number = input()
result = is_lapindrome(number)
print(result)