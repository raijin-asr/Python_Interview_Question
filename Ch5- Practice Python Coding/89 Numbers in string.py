# Complete the code below

# define a function
def digits_counter(string):

    count=0
    for ch in string:
        if ch.isdigit():
            count+=1
        
    return count


# call the function
string = input()
result = digits_counter(string)
print(result)