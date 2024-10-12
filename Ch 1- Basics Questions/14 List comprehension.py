# define a list
fruits = ['apple', 'banana', 'pineapple', 'mango', 'watermelon']

# using list comprehension, create another list
# that only contains the fruits that don't start with the  vowel letter
c_fruits = [fruit for fruit in fruits if fruit[0] not in 'aeiouAEIOU']

# print the new list
print(c_fruits)