numbers = [10,501,22,37,100,999,87,351]
count = 0
for num in numbers:
    temp=num
    seen=[]
    while temp != 1 and temp not in seen:
        seen.append(temp)
        s = 0
        while temp > 0:
            digit=temp % 10
            s=s+(digit * digit)
            temp=temp // 10
        temp=s
    if temp==1:
        count=count + 1
print("Total Happy Numbers:", count)
