#filter() is used to select elements from a list based on a condition.
# It keeps items that return True
#It removes items that return False
#it returns a iterators
#filter(function,iterators)

#filjtering age between 15 and 30
# def age(a):
#     if a>15 and a<30:
#         return a
# list_of_ages=[5,10,15,18,25,27]
# p=(list(filter(age,list_of_ages)))
# print(p)

#finding  odd or even
# def odd_even(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# list_of_ages=[5,10,15,18,25,27]
# p=(list(filter(odd_even,list_of_ages)))
# print(p)

lis=[5,10,15,18,25,27]
odd_even = lambda a : a%2==0
f=list(filter(odd_even,lis))
print(f)
