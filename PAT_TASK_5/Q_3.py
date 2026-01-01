num =[1,2,3,4,5,6,7,8]
even_num_sq = [
    n**2                #condition starts here square only even num
    for n in num
    if (lambda x: x % 2 == 0)(n)    #divisible by 2
]
print(even_num_sq)

