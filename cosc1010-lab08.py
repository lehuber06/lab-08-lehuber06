# Your Name Here: Lee Huber
# UWYO COSC 1010
# Submission Date: 11/4/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def int_or_float(num_str):    
    '''Put anything you want into the num_str string and watch the function work its magic'''
    number_list = num_str.split(".")
    num1 = number_list[0]
    if len(number_list) >= 2:
        del number_list[2:]
        num2 = number_list[1]

    if '.' in num_str and (num1 and num2).isnumeric():
        float_str = f"{num1}.{num2[0]}"
        return float(float_str)

    elif (number_list[0].isnumeric() or (len(number_list[0]) > 0 and number_list[0][0] == "-" and number_list[0][1:].isnumeric())) and len(number_list) == 1:
        return int(num_str)

    elif num_str.lower() == "exit":
        return "exit"
    
    else:
        return False

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(b, slope, lower_bound, upper_bound):
    for x in range(lower_bound, upper_bound + 1):
            print(f"\t({x}, {int_or_float(str((x*slope) + b))})")

while True:
    
    b = int_or_float(input("Type exit to exit\nEnter b here: "))
    if b == "exit":
        break
    while type(b) not in (int, float):
        b = int_or_float(input("Try again, enter b here: "))
        if b == "exit":
            break
    if b == "exit":
        break

    slope = int_or_float(input("Enter slope here: "))
    if slope == "exit":
        break
    while type(slope) not in (int, float):
        slope = int_or_float(input("Try again, enter slope here: "))
        if slope == "exit":
            break
    if slope == "exit":
        break

    lower_bound = int_or_float(input("Enter lower bound here (whole #'s only): "))
    if lower_bound == "exit":
        break
    while type(lower_bound) != int:
        lower_bound = int_or_float(input("Try again, enter lower bound here (whole #'s only): "))
        if lower_bound == "exit":
            break
    if lower_bound == "exit":
        break

    upper_bound = int_or_float(input("Enter upper bound here (whole #'s only): "))
    if upper_bound == "exit":
        break
    while type(upper_bound) != int:
        upper_bound = int_or_float(input("Try again, enter lower bound here (whole #'s only): "))
        if upper_bound == "exit":
            break
    if upper_bound == "exit":
        break

    print("All values below are in the form (y, x):")
        
    print(slope_intercept(b, slope, lower_bound, upper_bound))

print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqrt(num):
    if num > 0:
        return (num**.5)
    else:
        return False

def quadratic(a, b, c):
    sqroot = sqrt((b**2)-4*a*c)
    if sqroot != False:
        return f"Solution 1: {int_or_float(str((-b+sqroot)/(2*a)))}\nSolution 2: {int_or_float(str((-b-sqroot)/(2*a)))}"
    else:
        return False

while True:
    
    a = int_or_float(input("Type exit to exit\nEnter a here: "))
    if a == "exit":
        break
    while type(a) not in (int, float):
        a = int_or_float(input("Try again, enter a here: "))
        if a == "exit":
            break
    if a == "exit":
        break

    b = int_or_float(input("Enter b here: "))
    if b == "exit":
        break
    while type(b) not in (int, float):
        b = int_or_float(input("Try again, enter b here: "))
        if b == "exit":
            break
    if b == "exit":
        break


    c = int_or_float(input("Enter c here: "))
    if c == "exit":
        break
    while type(c) not in (int, float):
        c = int_or_float(input("Try again, enter c here: "))
        if c == "exit":
            break
    if c == "exit":
        break


    if quadratic(a, b, c) != False:
        print(quadratic(a, b, c))
    else:
        print("The solutions were imaginary, please try different values.")

