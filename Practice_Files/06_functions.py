
# Simple function to add two numbers

# define the function 
def add_numbers(a,b):
    c = a+b
    return c

# Call the function
output = add_numbers(5,10)  # 10 and 20 positional parameters
print(f"the sum of two number is: {output}")


# Keyword arguments
output = add_numbers(b=25, a=15)



# Multiple positional parameters
def multiply_numbers(*args):
    result = 1
    for num in args:
        result += num
    return result

output = multiply_numbers(2,3,4,5,6,7,8,9)
print(f"the multipilecation of number is: {output}")




# Multiple keyword arguments
def add_numbers(**kwargs):
    result = 1
    for key, value in kwargs.items():
        result += value
    return result

output = add_numbers(a=5, b=10, c=15)
print(f"the sum of keyword arguments is: {output}")




# Default arguments

def add_numbers(a, b=10):
    c = a + b
    return c

output = add_numbers(5)  # b will take the default value of 10 and a will take the value of 5
print(f"the sum of two number is: {output}")




# mix of positional, keyword and default arguments
def add_numbers(a, b=10, *args, **kwargs):
    result = a + b
    for num in args:
        result += num
    for key, value in kwargs.items():
        result += value
    return result

output = add_numbers(5, 15, 20, 25, c=30, d=35)
print(f"the sum of all arguments is: {output}")




# Lambda Function

addition = lambda x, y: x + y

result = addition(5, 10)
print(f"the sum of two number is: {result}")


# Using lambda function with user-defined function
