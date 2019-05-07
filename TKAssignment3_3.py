'''
Python Program to display the Fibonacci sequence up to nth term using recursive function
'''


def fibonacci(num):
    """
    Recursive function to print fibonacci sequence
    """
    return num if num <= 1 else fibonacci(num-1) + fibonacci(num-2)


# Number of terms required
nterms = 10

print("Fibonacci sequence")
for num in range(nterms):
    print(fibonacci(num))

