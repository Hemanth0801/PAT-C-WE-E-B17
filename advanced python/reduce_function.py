#reduce() is used to reduce a iterable to a single value by applying a function
from functools import reduce
list=[4,5,6]
add=lambda a,b:a+b   #first 2 num will add then+ next num(4+5, 6)
print(reduce(add,list))


