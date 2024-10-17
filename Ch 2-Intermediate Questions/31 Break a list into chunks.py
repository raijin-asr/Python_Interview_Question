
# define a list and empty list to store chunks
numbers = [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]
chunks = []

# start the loop from 0 to the length of the list,
# by step of 3 each time
for i in range(0,len(numbers),4):

    # from the list, take the 4 elements starting from i
    chunk = numbers[i:i+4]

    # append the chunk variable to the chunks list
    chunks.append(chunk)


# print the chunks list
for i in chunks:
    print(i)