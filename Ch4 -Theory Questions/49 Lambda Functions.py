# What is the Use of Lambda Functions in Python?
# In Python, a lambda function doesn't have a name and it can include only one expression. We use the lambda keyword to create a lambda function. For example,

# regular function
def add(x, y):
  return x + y

# lambda function
add = lambda x, y: x + y

# Here, x, y before : are the arguments, and x + y after : is the return value. We can call the above lambda function using:
add(4, 5)
# Output: 9