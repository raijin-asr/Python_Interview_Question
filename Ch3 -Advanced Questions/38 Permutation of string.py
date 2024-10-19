# define a function to find the permutation of a string
def get_permutation(string, i=0):

    # if i is the length of the string, print the string
    if i == len(string):
        print(''.join(string))

    # otherwise, for each character in the string,
    # swap it with the character at index i and recurse
    for j in range(i, len(string)):

        words = [c for c in string]
        # swap
        words[i], words[j] = words[j], words[i]

        # function recursion
        get_permutation(words, i + 1)

# call the function
get_permutation('ameer')