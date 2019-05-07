'''
Python Program to make a simple calculator that can add, subtract, multiply and division
'''


def add(a, b):
    """
    This function adds two numbers
    """
    return a + b


def multiply(a, b):
    """
    This function multiply two numbers
    """
    return a * b


def subtract(a, b):
    """
    This function subtract two numbers
    """
    return a - b


def division(a, b):
    """
    This function divides two numbers
    """
    return a / b


print("Select Option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    choice = int(input("Enter choice 1/2/3/4  :"))
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
except NameError:
    print("\nEnter a number only")
    pass

if choice == 1:
    print("Addition of {0} and {1} is {2}".format(num1, num2, add(num1, num2)))
elif choice == 2:
    print("Subtraction of {0} and {1} is {2}".format(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print("Multiplication of {0} and {1} is {2}".format(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print("Division of {0} and {1} is {2}".format(num1, num2, division(num1, num2)))
else:
    print("Invalid Choice")


