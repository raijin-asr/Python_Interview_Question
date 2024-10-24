# Complete the function below

# define a function
def character_counter(string):
    not_special=[]
    special=[]
    
    for i in string:
        if i.isalpha() or i.isdigit() or i.isspace():
            not_special.append(i)

        else:
            special.append(i)

    return len(special)

# call the function
string = input()
result = character_counter(string)
print(result)