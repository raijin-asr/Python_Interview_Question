# Complete the code below

# define a function
def count_common_vowel(string):

    vowel_dict={}
    string_split= string.split()
    for ch in string_split:
        if ch[-1] in "aeiou":
            vowel_dict[ch[-1]] = vowel_dict.get(ch[-1], 0) + 1

    max_vowel= max(vowel_dict.values())
    for val, ctr in vowel_dict.items():
        if ctr==max_vowel:
            return val

# call the function
string = input()
result = count_common_vowel(string)
print(result)