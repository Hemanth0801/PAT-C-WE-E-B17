#defined block of code which is used to peform a specific task
#can be defined keyword 'def'
#functions can have arguments
#function can return the value when needed
from ctypes import c_int16


# a=10
# b=10

# def trail():
#     pass   #pass is used  to function which does  not have any specific activity ,it cmplts body of a function
# trail()
# def addition():
#     print(a+b)
# addition()           #we need to call the function
# def subtraction():
#     print(a-b)
# subtraction()
# addition()

#declaring function
# def add (a=1,b=20):  #a and b are arguments / inputs which are passed to a function
#     print(a+b)
# add()
#
# def add (a,b):
#     print(a+b)
# add(10,20)


#converting the string to int

# a=(input("enter a")
# print(type(a))
# a= int(a)
# print(type(a))
# b=(input("enter b"))
# print(type(b))
# b=int(b)
# print(type(b))

#adding number by taking in cosole
# def add(a,b):
#     print(a+b)
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# add(a,b,c)

def add(a,b):
    return(a+b)    #return is used to return  the value

# x=1
# y=2
# add(x,y)

x=int(input("enter x"))
y=int(input("enter y"))
Z=int(input("enter Z"))
total=add(a=x,b=y)
print(total)
totalall= total + Z
print(totalall)