#type conversion is a method to convert a datatype of a particular variable
a='10'
b=20
print(type(a))
print(type(b))
a=int(a)
print(type(a))
print(a+b)

x=20
# x="20"
# print(type(x))

#int +float =float
y=10.0
z=x+y
print(type(z))
z=int(z)
print(type(z))

#int+bool=int
s= True
print(z+s)

c=-15     #ab s will return the positive num
print(abs(c))
