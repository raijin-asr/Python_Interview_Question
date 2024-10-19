
# define string that needs to be palindrome
# and counter to denote number of letters
# that should be added to make string palindrome
string = 'joe'
counter = 0

# loop till length of string is greater than 0
while len(string)>0:

    # if string is palindrome then break
    if string == string[::-1]:
        break

    # else add one to counter and remove last letter from string
    else:
        counter+=1
        string=string[:-1]

# print the counter variable
print(counter)