'''
Python Program to check given number is Prime or not (using break)
'''

try:
    num = int(input('Enter a number: '))
except NameError:
    print("\nEnter a number only")
    pass

isDivisible = False
i = 2

while i < num:
    if num % i == 0:
        isDivisible = True
        print("{} is divisible by {}".format(num, i))
        break  # this line is the only addition
    i += 1

if isDivisible:
    print("{} is NOT a Prime number".format(num))
else:
    print("{} is a Prime number".format(num))
