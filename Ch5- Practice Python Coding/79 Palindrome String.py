# Complete the function below

# define a function
def is_palindrome(string):

    result=""
    for i in string:
        if i.isdigit():
            del i
        
        if not i.isalpha():
            del i

        else:
            result+=i

    if result.lower() == result[::-1].lower():
        return "String is Palindrome"
    
    else:
        return "String is not Palindrome"


# call the function
string = input()
result = is_palindrome(string)
print(result)