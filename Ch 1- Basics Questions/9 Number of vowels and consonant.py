# define a function to count vowels and consonants in a string
def count_vowels_and_consonants(string):

    # define a list of vowels to be removed
    vowels = 'aeiouAEIOU'

    # initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # loop through each character in the string
    for char in string:

        # if the character is a vowel, increment the vowel counter
        if char in vowels:
            vowel_count += 1

        # if the character is a space, continue to the next character
        elif char==" ":
            continue

        # else, increment the consonant counter
        else:
            consonant_count+=1

    # print vowels and consonants count
    print('Vowels: '  + str(vowel_count))
    print('Consonants: ' + str(consonant_count))


# call the function
string = 'A quick brown fox jumps over the lazy dog'
count_vowels_and_consonants(string)