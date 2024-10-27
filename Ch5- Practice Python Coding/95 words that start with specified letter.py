# Complete the code below

# define a function
def words_start_with(string, letter):

    string= string.split()
    new_string=[]
    for word in string:
        if word[0]==letter:
            new_string.append(word)
    return new_string


# call the function
string = input()
letter = input()
result = words_start_with(string, letter)
print(result)