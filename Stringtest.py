message = "Hello World"
# print(len(message))

# Extracting "Hello" word using while loop
i = 0
Omessage = ''
while(i < 6):
    Omessage += message[i]
    i = i + 1
print(Omessage)

# Extracting "Hello" word using slicing
print(message[0:5])
print(message[6:])

# Counting number of occurences using count.
# returns -1 if it cannot find occurence
print(message.count('l'))

message = message.replace('World', 'Universe')

print(message)

# Using placeholders
greet = 'Hello'
name = 'Abhishek'
message = '{}, {}. Welcome!'.format(greet, name)
print(message)

# Alternate f string
message = f'{greet}, {name.upper()}. Welcome!'
print(message)

# Finding Help
# print(help(str))
print(help(str.find))
print(help(str.replace))
