from functools import reduce

num = [12,3,40,12,13,14,41]
add = lambda a,b:a+b
print(reduce(add,num))
