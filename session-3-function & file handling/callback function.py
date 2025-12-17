# a function is created for a particular task
# calling a function with its name , activates the function excution

#callback function is function which is passed as an argument

# def greet(name):
#     print("Hello", name)
#
# def welcome(callback):
#     callback("Hemanth")   # calling the passed function
#
# welcome(greet)

def greet(name):
    print("hello",name)

def funct(callback, name):
    callback(name)

funct(greet,"hemu")

#addition and subtraction
# def add(a,b):
#      return(a+b)
#
# def sub(a,b):
#     return(a-b)
#
# def final(x,y):
#     print(add(x,y))
#     print(sub(x,y))
#
# final(1,2)



