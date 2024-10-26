# Complete the code below

# define a function
def vowel_repeater(string, n):

    list=[]
    for ch in string:
        if ch not in "aeiou":
            list.append(ch)

        else:
            for i in range(1,n+1):
                list.append(ch)

    return "".join(list)

# call the function
string = input()
n = int(input())
result = vowel_repeater(string, n)
print(result)