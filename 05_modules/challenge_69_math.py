#importing a math module

import math

numb1 = float(input("Enter a number: "))

#Calculating the square root of a float number
result = math.sqrt(numb1)

print("Square Root of a Number is {}".format(result))

print("Rounded-up result value", math.ceil(result))

print("Rounded-down result value", math.floor(result))