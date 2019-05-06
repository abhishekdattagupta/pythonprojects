'''
Python Program to sort words in Alphabetical order
'''

myStr = "python Program to Sort words in Alphabetical Order"

words = myStr.split()
words.sort()
for word in words:
    print(word)

