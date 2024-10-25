# Complete the code below

# define a function
def duplicate_counter(string):

    dict_counter={}
    string=string.lower()
    for itm in string:
        if itm.isalpha():
            dict_counter[itm]= dict_counter.get(itm,0)+1
        
    dup_count=0
    for count in dict_counter.values():
        if count >1:
            dup_count+=1
    return dup_count

# call the function
string = input()
result = duplicate_counter(string)
print(result)