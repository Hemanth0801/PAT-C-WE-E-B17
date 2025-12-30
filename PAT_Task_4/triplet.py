#trpilet- comb of 3values = 59

num = [10,20,30,9]
value = 59
n=len(num)       #length of num=4
for i in range(n):     #0,1,2,3,
    for j in range(i+1,n):
        for k in range(j+1,n):
            if num[i]+num[j]+num[k]==value:
                print("triplet found: ", num[i],num[j],num[k])

