#lambda function is a anonymus functions,one-line functions are for short operations
#created using lambda keyword
#lambda functions are created on a fly
#syntax  for lambda
#_my_lambda_fun = lambda argument:expressiom

#normal function
# def add(a,b):
#     return a+b
#
# print(add(1,2))

#_my_lambda_fun = lambda argument:expressiom
num_sqr = lambda x: x**2
print(num_sqr(5))
num_add = lambda c,d: c + d  #add of 2variables
print(num_add(1,2))
# z='49238123'
# print(len(z))
z=lambda e:len(e)
print(z("123144"))
g=lambda h:max(h)
print(g('2345'))
check_odd_even=lambda b:"even" if b%2==0  else "odd"
print(check_odd_even(3))






