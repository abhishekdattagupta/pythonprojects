'''
Python Program to check given number is Prime number or not
'''

try:
    num1 = int(input('Enter a number: '))
except NameError:
    print("\nEnter a number only")
    pass

isDivisible = False
i = 2
while i < num1:
    if num1 % i == 0:
        isDivisible = True
        print("{} is divisible by {}".format(num1, i))
    i += 1

if isDivisible:
    print("{} is NOT a Prime number".format(num1))
else:
    print("{} is a Prime number".format(num1))
