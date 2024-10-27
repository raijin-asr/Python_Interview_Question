# Complete the code below

#  define a function that cleans the string
def improve_english(string):
    string= string[0].upper() + string[1:].lower()
    new_string= string.strip()+ "."
    return new_string


# call the function
string = input()
result = improve_english(string)
print(result)