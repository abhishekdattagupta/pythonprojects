def hello_func():
    pass


print(hello_func())


def hello_func():
    return "Hello"


print(hello_func())
print(hello_func().upper())


def hell_fun(greet, name='Abhishek'):
    return f'{greet}, {name} Function'


print(hell_fun('Hi'))

# *args allow arbitrary number of positional argumants
# may return a tuple
# **kwargs allow arbitrary number of keyword argumants
# may return a dictionary with all keyword values


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# student_info('Math', 'Art', name='abhishek', age=38)
# Output
# ('Math', 'Art')
# {'name': 'abhishek', 'age':38}

courses = ['Math', 'Art']  # We have a list
info = {'name': 'abhishek', 'age': 38}  # we have a dictionary

student_info(*courses, **info)
# * and ** unpacks the valuesof the list and dictionary
