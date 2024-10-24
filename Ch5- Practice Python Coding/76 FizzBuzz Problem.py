# Complete the function below

# define a function
def fizzbuzz(n):

    list=[]
    for i in range(1,n+1):
        if i%3==0:
            list.append("Fizz")

        elif i%5==0:
            list.append("Buzz")

        else:
            list.append(str(i))

    return list


# call the function
number = int(input())
output = fizzbuzz(number)
print(output)