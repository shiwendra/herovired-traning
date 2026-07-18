# Function in Python    
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
#  A function can return data as a result.
## You can use the def keyword to create a function.       
#inbuilt functions are the functions that are already defined in Python. You can use them without defining them.
# print() is an inbuilt function that prints the specified message to the screen, or other standard output device.
#type() is an inbuilt function that returns the type of the specified object.
#input() is an inbuilt function that allows user input.
#len() is an inbuilt function that returns the length of an object.
#User-defined functions are the functions that are defined by the user to perform specific tasks.
#  You can define your own functions using the def keyword.
## Syntax
# def function_name(parameters): 
#Example of a user-defined function that takes two parameters and returns their sum:
#*args allows you to pass a variable number of arguments to a function. It collects any additional positional arguments passed to the function into a tuple. 
def add_numbers(num1, num2, *args):
    total = num1 + num2
    for n in args:
        total += n
    return total

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# User enters: 10, 20, 30, 40
c = list(map(int, input("Enter numbers separated by comma: ").split(',')))
result = add_numbers(a, b, *c)  
print("The sum is:", result)