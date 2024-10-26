# Complete the code below

# define a function
def calculate_bmi(weight, height):

    BMI= weight / height **2
    if BMI < 18.5:
        return "Underweight"
    elif BMI >=18.5 and BMI <=24.9:
        return "Normal Weight"
    elif BMI >=25.0 and BMI <= 29.9:
        return "Overweight"
    else:
        return "Obese"

# call the function
weight = float(input())
height = float(input())
result = calculate_bmi(weight, height)
print(result)