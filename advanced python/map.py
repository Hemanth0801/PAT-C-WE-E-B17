#map() is used to apply a function to every item in a list (or any iterable)
#and get the result.


# def sq_num(a):
#     return a**2
# list_1=[1,2,3]
#
# squar_num=map(sq_num,list_1)
# print(squar_num)

#if u have a map done function what is return time (return time would be an map obj)

#convert into ,ist &tuple
def sq_num(a):
    return a**2
list_1=[1,2,3]

squar_num=tuple(map(sq_num,list_1))
print(squar_num)

#lambda function in map()
# def sq_num(a):
#     return a**2
list_1=[1,2,3]
sq_num=lambda x:x**2

squar_num=list(map(sq_num,list_1))
print(squar_num)

