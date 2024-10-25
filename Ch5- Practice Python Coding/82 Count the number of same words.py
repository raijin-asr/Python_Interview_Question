# Complete the code below

# define a function
def same_word_counter(string):
    string=string.lower()

    words= string.split()
    word_dict={}

    for word in words:
        word = "".join([char for char in word if char.isalpha()])
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

# call the function
string = input()
result = same_word_counter(string)
print(result)
