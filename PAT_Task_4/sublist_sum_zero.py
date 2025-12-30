num=[4,2,-3,1,6]
n=len(num)
found= False
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = sum + num[j]
        if sum == 0:
            found= True
            print("found")
            break
    if found:
        break
if not found:
    print("not found")