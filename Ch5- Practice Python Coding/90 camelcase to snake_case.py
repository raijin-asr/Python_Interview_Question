# Complete the code below

# define a function
def camel_to_snake_case(string):

    new= ""
    for ch in string:
        if ch.isupper():
            new+="_"+ ch.lower()
        else:
            new+=ch
    return new

# call the function
string = input()
result = camel_to_snake_case(string)
print(result)