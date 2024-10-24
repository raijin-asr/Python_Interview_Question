# Complete the function below

# define a function
def unique_character(string):
   for i, ch in enumerate(string):  # Iterate through indices
        if ch.lower() not in string[i+1:].lower():
            return i  # Return the index of the unique character

# call the function
string = input()
result = unique_character(string)
print(result)