num=[10,501,22,37,100,999,87,35]
primenumber=[]  #prime will store here
for i in num:
    if i > 1 :      #prime num should be greater than 1
        is_prime=True
        for j in range(2,i):  #range never includes the last value(num-1)
            if i % j == 0:    #is the remainder is 0 not prime
                is_prime=False
                break
        if is_prime:
            primenumber.append(i)
print(primenumber)
print(len(primenumber))

