'''
Python Program to check whether a string is Palindrome or not
'''

myStr = "Madam"
myStr = myStr.lower()

revStr = reversed(myStr)

if list(myStr) == list(revStr):
    print("Given string {0} is Palindrome".format(myStr))
else:
    print("Given string is not Palindrome")
