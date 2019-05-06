'''
Python program to find the largest element among three Numbers
'''

try:
    num1 = int(input('Enter first non-zero input value > '))
    num2 = int(input('Enter second non-zero input value > '))
    num3 = int(input('Enter third non-zero input value > '))
except ValueError:
    print("\nEnter a number only")
    pass
print(num1, num2, num3)
if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("Largest element among three numbers is: {}".format(largest))