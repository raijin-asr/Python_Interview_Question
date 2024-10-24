# Complete the function below

# define a function
def bill_splitter(amount, persons):

    tax=8.875
    each_pay= round(amount/persons + (tax / 100) * (amount/persons),5)
    return each_pay
    
# call the function
amount = float(input())
persons = int(input())
result = bill_splitter(amount, persons)
print(result)