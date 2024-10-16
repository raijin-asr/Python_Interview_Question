
# function that reverses a string word by word
def reverse_by_word(sentence):

    # split the sentence into words
    words_list = sentence.split(" ")

    # reverse the words in the list
    reversed_words_list = words_list[::-1]

    # join the words in the list into a sentence
    result = " ".join(reversed_words_list)

    print(result)


# call the function with the parameter
reverse_by_word('this is blue')