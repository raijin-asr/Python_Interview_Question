# Complete the code below

# define a function
def semi_reverse(string):

    string= string.split()
    reverse_list=[]

    for itm in string:
        if len(itm)%2!=0:
            itm= itm[::-1]
            reverse_list.append(itm)

        else:
            reverse_list.append(itm)

    result= " ".join(reverse_list)
    return result


# call the function
string = input()
result = semi_reverse(string)
print(result)