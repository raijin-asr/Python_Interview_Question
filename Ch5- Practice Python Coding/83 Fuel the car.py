# Complete the code below

# define a function
def required_fuel(kms):

    stock_fuel= 100
    extra_fuel=0
    total_required_fuel= kms * 10
    if kms<10:
        extra_fuel= 0
    else:
        extra_fuel= total_required_fuel- stock_fuel

    return (total_required_fuel, extra_fuel)

# call the function
kms = int(input())
result = required_fuel(kms)
print(result)