#Lab:
#Write a Python program to create a function that takes a string as input and prints it.

def string(input_string):
    print(input_string)

string("Hello, World!")

# Write a Python program to create a calculator using functions.

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


num1 = 15
num2 = 5
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

#19) Write a Python program to print a string using a function. 

def print_string(input_string):
    print(input_string)

print_string("Hello, Python!")

# 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum. 

def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 3)

# 21) Write a Python program to create a lambda function with one expression. 

# Lambda function to add two numbers
add = lambda a, b: a + b 

print(add(5, 3))

# 22) Write a Python program to create a lambda function with two expressions.


process = lambda a, b: (a + b, a * b)

result = process(1, 3)
print("Sum:", result[0], "Product:", result[1])

