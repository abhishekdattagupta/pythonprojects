'''
Python Program to display all prime numbers within an interval
'''

try:
    index1 = int(input('Input Start index to provide range to check for prime numbers: '))
    index2 = int(input('Input End index to provide range to check for prime numbers: '))
except NameError:
    print("\nEnter a number only")
    pass
# print(index1, index2)
print("Prime numbers between {0} and {1} are :".format(index1, index2))

for num in range(index1, index2 + 1):
    # default step size is 1
    if num > 1:
        isDivisible = False
        for index in range(2, num):
            if num % index == 0:
                isDivisible = True
        if not isDivisible:
            print(num)


